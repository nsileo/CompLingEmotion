from textblob import TextBlob
from collections import Counter
import re

def find_punctuations(text, mark):
    mark = "\\" + mark
    pattern = re.compile(mark)
    occur = re.findall(mark, text)

    return len(occur)

def find_all_punctuations(text):
    punctuations = ['!', "?", ':', ";", '.', ',', '(', ')']
    punctuations_dict ={}
    for mark in punctuations:
        mark = "\\" + mark
        pattern = re.compile(mark)
        occur = re.findall(mark, text)
        mark=mark[1:]
        punctuations_dict[mark]=len(occur)


    return punctuations_dict