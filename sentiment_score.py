import nltk.sentiment.vader
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
import pandas
import numpy as np

from NRCLexPkg.nrclex import NRCLex

df = pandas.read_csv('mypersonality_final.csv',
                     header=0)
print(df.head())
test = "This is bad news! I am hopeful to see how it turns out. I am anxious"
test_bad = "This was not that badly good for me! i could not resist"
analyzer = nltk.sentiment.vader.SentimentIntensityAnalyzer()
print(analyzer.polarity_scores(test))

no_emotion = 0
for status_update in df["STATUS"]:
    # print(analyzer.polarity_scores(status_update))
    emotions_object = NRCLex(status_update)
    print(emotions_object.raw_emotion_scores)
    if len(emotions_object.raw_emotion_scores) == 0:
        no_emotion += 1

print(no_emotion / len(df["STATUS"]))

emotions_object_test = NRCLex(test)
print(emotions_object_test.raw_emotion_scores)

print(analyzer.polarity_scores(test))
