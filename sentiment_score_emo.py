import pandas as pd
import punctuation_analyzer

from NRCLexPkg.nrclex_emo import NRCLex

df = pd.read_csv('mypersonality_final.csv',
                     header=0)
#print(df.head())
test = "This is bad news! I am hopeful to see how it turns out. I am anxious"
test_bad = "This was not that badly good for me! i could not resist"
test_emoticons = "0.o"



positive = list()
negative = list()
joy= list()
sadness = list()
fear = list()
disgust =list()
anticipation = list()
surprise = list()
punctuation = list()
sum_emotions = list()

noEmotes = []
no_emotion = 0
for status_update in df["STATUS"]:
    emotions_object = NRCLex(status_update)
    #print(emotions_object.raw_emotion_scores)
    if len(emotions_object.raw_emotion_scores) == 0:
        no_emotion += 1
        noEmotes.append(emotions_object.text)
    positive.append(0)
    negative.append(0)
    joy.append(0)
    sadness.append(0)
    fear.append(0)
    disgust.append(0)
    anticipation.append(0)
    surprise.append(0)
    punctuation.append(0)
    sum_emotions.append(0)
    for emo in ["positive","negative", "sadness","joy","fear","surprise","disgust", "anticipation"]:
        if (emo in emotions_object.raw_emotion_scores.keys() and emo =="positive"):
            positive[-1] = (emotions_object.raw_emotion_scores[emo])
            sum_emotions[-1] +=(emotions_object.raw_emotion_scores[emo])

        if ( emo == 'negative' and emo in emotions_object.raw_emotion_scores.keys()):
            negative[-1] = (emotions_object.raw_emotion_scores[emo])
            sum_emotions[-1] +=(emotions_object.raw_emotion_scores[emo])

        if ( emo == 'joy' and emo in emotions_object.raw_emotion_scores.keys()):
            joy[-1] = (emotions_object.raw_emotion_scores[emo])
            sum_emotions[-1] +=(emotions_object.raw_emotion_scores[emo])


        if ( emo == 'sadness' and emo in emotions_object.raw_emotion_scores.keys()):
            sadness[-1]= (emotions_object.raw_emotion_scores[emo])
            sum_emotions[-1] +=(emotions_object.raw_emotion_scores[emo])

        if ( emo == 'fear' and emo in emotions_object.raw_emotion_scores.keys()):
            fear[-1] = (emotions_object.raw_emotion_scores[emo])
            sum_emotions[-1] +=(emotions_object.raw_emotion_scores[emo])

        if ( emo == 'disgust' and emo in emotions_object.raw_emotion_scores.keys()):
            disgust[-1] = (emotions_object.raw_emotion_scores[emo])
            sum_emotions[-1] +=(emotions_object.raw_emotion_scores[emo])


        if ( emo == 'anticipation' and emo in emotions_object.raw_emotion_scores.keys()):
            anticipation[-1] = (emotions_object.raw_emotion_scores[emo])
            sum_emotions[-1] +=(emotions_object.raw_emotion_scores[emo])

    #create punctuation predictor
    question = punctuation_analyzer.find_punctuations(status_update, '?')
    exclamation = punctuation_analyzer.find_punctuations(status_update, '!')
    #period = punctuation_analyzer.find_punctuations(status_update, '.')
    qu_ex_sum = question + exclamation
    if qu_ex_sum != 0 :
        punctuation[-1] = qu_ex_sum


data = df.iloc[:,[0,2,3,4,5,6,13]]
data = data.assign(positive = positive)
data = data.assign(negative = negative)
data = data.assign(joy = joy)
data = data.assign(sadness = sadness)
data = data.assign(fear = fear)
data = data.assign(disgust = disgust)
data = data.assign(anticipation = anticipation)
data = data.assign(surprise = anticipation)
data = data.assign(sum_emotions = sum_emotions)
data = data.assign(punctuation = punctuation)
print(data.tail())

data.to_csv('continuous_outcome_emo.csv')

print('Coverage:' , no_emotion / len(df["STATUS"]))
