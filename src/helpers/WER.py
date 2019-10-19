import numpy as np
from jiwer import wer
import re


def wer_score(hyp, sent):
    """
    Calculate WER for 1 or several sentences
    """

    delimiters = ". ", "? ", "! "
    regexPattern='|'.join(map(re.escape, delimiters))
    transcript = re.split(regexPattern, hyp)

    label = re.split(regexPattern, sent)

    return wer(label, transcript)
