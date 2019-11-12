from fastai.text import load_learner, List, BaseTokenizer, Tokenizer
from pytorch_pretrained_bert import BertTokenizer


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

class Config(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def set(self, key, val):
        self[key] = val
        setattr(self, key, val)


def predict_label(PATH_TO_MODEL, speech):
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
    return fastai_tokenizer

    # learner = load_learner(PATH_TO_MODEL)
    # return learner.predict(speech)[0]

#print(learner.predict("My foot hurts after playing football")[0])
