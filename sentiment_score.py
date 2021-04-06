import pandas as pd



from NRCLexPkg.nrclex import NRCLex

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
    for emo in ["positive","negative", "sadness","joy","fear","surprise","disgust", "anticipation"]:
        if ( emo in emotions_object.raw_emotion_scores.keys() and emo =="positive"):
            positive[-1] = (emotions_object.raw_emotion_scores[emo])


        if ( emo == 'negative' and emo in emotions_object.raw_emotion_scores.keys()):
            negative[-1] = (emotions_object.raw_emotion_scores[emo])


        if ( emo == 'joy' and emo in emotions_object.raw_emotion_scores.keys()):
            joy[-1] = (emotions_object.raw_emotion_scores[emo])



        if ( emo == 'sadness' and emo in emotions_object.raw_emotion_scores.keys()):
            sadness[-1]= (emotions_object.raw_emotion_scores[emo])


        if ( emo == 'fear' and emo in emotions_object.raw_emotion_scores.keys()):
            fear[-1] = (emotions_object.raw_emotion_scores[emo])


        if ( emo == 'disgust' and emo in emotions_object.raw_emotion_scores.keys()):
            disgust[-1] = (emotions_object.raw_emotion_scores[emo])



        if ( emo == 'anticipation' and emo in emotions_object.raw_emotion_scores.keys()):
            anticipation[-1] = (emotions_object.raw_emotion_scores[emo])


data = df.iloc[:,[2,3,4,5,6]]
data = data.assign(positive = positive)
data = data.assign(negative = negative)
data = data.assign(joy = joy)
data = data.assign(sadness = sadness)
data = data.assign(fear = fear)
data = data.assign(disgust = disgust)
data = data.assign(anticipation = anticipation)
print(data.tail())

data.to_csv('continous_outcome.csv')

print(no_emotion / len(df["STATUS"]))

#print(len(fear))
#print(positive[0:10])
#emotions_object_test = NRCLex(test)
#print(emotions_object_test.raw_emotion_scores)


#print("\ntest_emoticons: ")
#emotions_object_test_emoticons = NRCLex(test_emoticons)
#print(emotions_object_test_emoticons.raw_emotion_scores)