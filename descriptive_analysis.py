
import pandas as pd

import numpy as np



#generate preditions for nrclex with emoticons (nrclex_emo)
data = pd.read_csv('continuous_outcome_emo_lem.csv',
                     header=0)
#select unique users to be test data
data['sEXT'].loc[(data['sEXT'] < 3.6)] = 0
data['sEXT'].loc[(data['sEXT'] >= 3.6)] = 1
data['sOPN'].loc[(data['sOPN'] < 3.8)] = 0
data['sOPN'].loc[(data['sOPN'] >= 3.8)] = 1
data['sAGR'].loc[(data['sAGR'] < 3.55)] = 0
data['sAGR'].loc[(data['sAGR'] >= 3.55)] = 1
data['sCON'].loc[(data['sCON'] < 3.5)] = 0
data['sCON'].loc[(data['sCON'] >= 3.5)] = 1
data['sNEU'].loc[(data['sNEU'] < 2.8)] = 0
data['sNEU'].loc[(data['sNEU'] >= 2.8)] = 1

#get correlations
for trait in ['sEXT', 'sOPN', 'sAGR','sCON','sNEU']:
    correlation = list()
    for senti in ["NETWORKSIZE", "positive","negative", "sadness","joy","fear","surprise","disgust", "anticipation"]:
        correlation.append(np.corrcoef(data[trait],data[senti]))

    print(trait, correlation)

traits = list()
sentis = list()
probs= list()

for trait in ['sEXT', 'sOPN', 'sAGR','sCON','sNEU']:
    #get rows with trait = 1 (or 0)
    data_trait = data[data[trait] == 1]
    sum_trait = np.sum(data[trait] == 1)

    for senti in ["positive","negative", "sadness","joy","fear","surprise","disgust", "anticipation", "sum_emotions"]:
        if senti == 'sum_emotions':
            sum_trait_senti = data_trait[data_trait[senti] == 0]

            sum_trait_senti = len(sum_trait_senti[senti])
            senti = "no_emotion"
        else:
            sum_trait_senti = data_trait[data_trait[senti] > 0]
            sum_trait_senti = np.count_nonzero(sum_trait_senti[senti])


        probability = (sum_trait_senti)/sum_trait
        traits.append(trait)
        sentis.append(senti)
        probs.append(probability)
        print(trait, senti, probability)

conditional_probability = pd.DataFrame(zip(traits,sentis,probs))
conditional_probability.to_csv('conditional_probabilities_yes.csv')