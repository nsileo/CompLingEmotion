from textblob import TextBlob
from collections import Counter
import re

def find_punctuations(text, mark):
    mark = "\\" + mark
    pattern = re.compile(mark)
    occur = re.findall(mark, text)

    return len(occur)