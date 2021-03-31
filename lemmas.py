# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:02:14 2021
@author: nicks
"""

from nltk.stem.snowball import SnowballStemmer
from nltk.stem.porter import *
#Subsection of the lexicon
miniLex = {
'anguish': ['anger', 'fear', 'negative', 'sadness'], 'animate': ['positive'],
               'animated': ['joy', 'positive'], 'animosity': ['anger', 'disgust', 'fear', 'negative', 'sadness'],
               'animus': ['anger', 'negative'], 'annihilate': ['anger', 'fear', 'negative'],
               'annihilated': ['anger', 'fear', 'negative', 'sadness'],
               'annihilation': ['anger', 'fear', 'negative', 'sadness'], 'announcement': ['anticipation'],
               'annoy': ['anger', 'disgust', 'negative'], 'annoyance': ['anger', 'disgust', 'negative'],
               'annoying': ['anger', 'negative'], 'annul': ['negative'], 'annulment': ['negative', 'sadness'],
               'anomaly': ['fear', 'negative', 'surprise'], 'anonymous': ['negative'], 'answerable': ['trust'],
               'antagonism': ['anger', 'negative'], 'antagonist': ['anger', 'negative'],
               'antagonistic': ['anger', 'disgust', 'negative'], 'anthrax': ['disgust', 'fear', 'negative', 'sadness'],
               'antibiotics': ['positive'], 'antichrist': ['anger', 'disgust', 'fear', 'negative'],
               'anticipation': ['anticipation'], 'anticipatory': ['anticipation'],
               'antidote': ['anticipation', 'positive', 'trust'], 'antifungal': ['positive', 'trust']
}

stemmer = SnowballStemmer("english")
#stemmer = PorterStemmer()

def lemmaAdder(dicToStem):
    stems = {}
    
    #Iterate over every word
    for word in dicToStem:
        #Take emotions of that original word
        #print(word)    #Debug line
        emotes = dicToStem[word]
        
        #Apply Stemmer
        stem = stemmer.stem(word)
        
        #Check if stem already in
        if stem not in stems and stem not in dicToStem:
            #If stem has not been added yet, add it
            stems[stem] = emotes
            #print(stem, ' added')     #Debug line
        
        #Debug statements to see what types of stems are not being added and why
#        else:
#            if stem in stems:
#                print(stem, 'is already in stems, not added')
#            if stem in dicToStem:
#                print(stem, 'is already in dicToStem, not added')
        
    #dicToStem has been fully processed and stems should be filled
    #Combine them into one dict
    combDict = dict(stems)       #Makes copy of stems
    combDict.update(dicToStem)   #Adds entries of dicToStem to the copy
    
    #print(stems.keys())         #Debug- Uncomment to see only the stems added
    
    return combDict
    
    
combinedDict = lemmaAdder(miniLex)

#print(miniLex['animation'])    #This causes key error since animation is not in the lexicon

#This prints ['positive'] since it stems to 'anim', which inherited its emotions from
#the word 'animate'
print(combinedDict[stemmer.stem('animation')])
