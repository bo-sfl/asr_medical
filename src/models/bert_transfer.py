'''
This script is used to train a text classification model with BERT.
'''

import csv
import pandas as pd
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from typing import *
#import matplotlib.cm as cm

import torch
import torch.optim as optim
from pytorch_pretrained_bert import BertTokenizer
from pytorch_pretrained_bert.modeling import BertConfig, BertForSequenceClassification

from fastai import *
from fastai.text import *
from fastai.callbacks import *
from fastai.metrics import *



class Config(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def set(self, key, val):
        self[key] = val
        setattr(self, key, val)

class FastAiBertTokenizer(BaseTokenizer):
    """Wrapper around BertTokenizer to be compatible with fast.ai"""
    def __init__(self, tokenizer: BertTokenizer, max_seq_len: int=128, **kwargs):
        self._pretrained_tokenizer = tokenizer
        self.max_seq_len = max_seq_len

    def __call__(self, *args, **kwargs):
        return self

    def tokenizer(self, t:str) -> List[str]:
        """Limits the maximum sequence length"""
        return ["[CLS]"] + self._pretrained_tokenizer.tokenize(t)[:self.max_seq_len - 2] + ["[SEP]"]

def load_data(f_path):
    df = pd.read_csv(f_path)
    return df[["phrase", "prompt"]]

def split_data(df):
    train, test = train_test_split(df)
    train, val = train_test_split(train)
    print(f'Train data length:{len(train)}, \
            valid data length:{len(val)},  \
            test data length:{len(test)}') 
    return train, test, val

def model_build(train, val):
    config = Config(
        testing=False,
        bert_model_name="bert-base-uncased",
        max_lr=3e-5,
        epochs=4,
        use_fp16=True,
        bs=32,
        discriminative=False,
        max_seq_len=256,
    )


    bert_tok = BertTokenizer.from_pretrained(
        config.bert_model_name,
    )

    fastai_tokenizer = Tokenizer(tok_func=FastAiBertTokenizer(bert_tok, max_seq_len=config.max_seq_len), pre_rules=[], post_rules=[])

    fastai_bert_vocab = Vocab(list(bert_tok.vocab.keys()))

    databunch = TextDataBunch.from_df(".", train, val,
                    tokenizer=fastai_tokenizer,
                    vocab=fastai_bert_vocab,
                    include_bos=False,
                    include_eos=False,
                    text_cols="phrase",
                    label_cols="prompt",
                    bs=config.bs,
                    collate_fn=partial(pad_collate, pad_first=False, pad_idx=0),
                )

    bert_model = BertForSequenceClassification.from_pretrained(config.bert_model_name, num_labels=len(databunch.classes))


    learner = Learner(
        databunch, bert_model,
        metrics=[accuracy]
    )
    #learner.callbacks.append(ShowGraph(learner))
    return learner

def model_train(learner):
    learner.fit_one_cycle(4, max_lr=1e-5)
    learner.fit_one_cycle(4, max_lr=2e-5)
    learner.export()
    return

def model_predict(learner, test):
    score = 0
    for _, row in test.iterrows():
        if str(learner.predict(row.phrase)[0]) == row.prompt:
            score +=1
    print("acc in test", score/len(test))
    return

def main():
    data = load_data("data.csv")
    train, test, val = split_data(data)
    learner = model_build(train, test)
    model_train(learner)
    model_predict(learner, test)
    return learner

if __name__ == "__main__":
    main()