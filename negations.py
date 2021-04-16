# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:45:33 2021

@author: nicks
"""


stat0 = "Where is the negation in this sentence?"
stat1 = "is having a bad day. not even target, shoes, nor a good guacamole carls jr. burger could bring me up."
stat2 = "UGGGGGGHHHHH! My WoW account is totally screwed up and now they've \"permanently disabled\" it. So not cool!"
stat3 = "just found out Chinese New Year is on Valentine's Day... that makes two holidays I have no one to celebrate with... and no, I'm not sulking"
stat4 = "People should not encourage me to drink until 4 o'clock in the morning and party all night long :("
stat5 = "I like to drink until 4 in the morning, but it is not good for me"
stat6= "If you had not slept the whole day, you would have enjoyed the sun"
neg_words = ["no", "not", "rather", "couldn’t", "wasn’t", "didn’t", "wouldn’t",
             "shouldn’t", "weren’t", "don’t", "doesn’t", "haven’t", "hasn’t", 
             "won’t", "wont", "hadn’t", "never", "none", "nobody", "nothing",
             "neither", "nor", "nowhere", "isn’t", "can’t", "cannot", "mustn’t",
             "mightn’t", "shan’t", "without", "needn’t"]

NEGATE = [ "aint", "arent", "cannot", "cant",
        "couldnt", "darent", "didnt", "doesnt",
        "ain't", "aren't", "can't", "couldn't",
        "daren't", "didn't", "doesn't", "dont",
        "hadnt", "hasnt", "havent", "isnt",
        "mightnt", "mustnt", "neither", "don't",
        "hadn't", "hasn't", "haven't", "isn't",
        "mightn't", "mustn't", "neednt", "needn't",
        "never", "none", "nope", "nor", "no",
        "not", "nothing", "nowhere", "oughtnt",
        "shant", "shouldnt", "uhuh", "wasnt",
        "werent", "oughtn't", "shan't", "shouldn't",
        "uh-uh", "wasn't", "weren't", "without",
        "wont", "wouldnt", "won't", "wouldn't",
        "rarely", "seldom", "despite"]

conj_cond = ["if", "unless", "when"]
conj_addComp = ["and", "moreover", "additionally", "further",
             "furthermore", "also", "plus"]
conj_cont = ["but", "however", "instead"]

import pandas as pd
import punctuation_analyzer
import nltk

from NRCLexPkg.nrclex_base import NRCLex

df = pd.read_csv('mypersonality_final.csv', header=0)

def negationAnalyzer(status):
    #Tokenize the status
    stat = nltk.word_tokenize(status)
    
    #Checks for negation words in the tokens
    hasNeg = True in (tok in neg_words for tok in stat)
    if hasNeg == True:
        #This status has a negation word
        print("Contains Negation Word")
        
        #Cut out first and last tokens- they do not matter if they are conjunctions
        subStat = stat[1:-1]
        idealPos = len(subStat)/2
        
        #Need to check for conjunctions
        conjType = "None"
        conjLoc = -1
        curPos = 0
        bestDist = 99
        
        #Gets counts of each, finds the one closest to middle to be the priority conjunction
        for word in subStat:
            if word in conj_cond:
                if abs(curPos-idealPos) < bestDist:
                    conjType = "cond"
                    bestDist = abs(curPos-idealPos)
                    conjLoc = curPos
                    
            if word in conj_addComp:
                if abs(curPos-idealPos) < bestDist:
                    conjType = "addComp"
                    bestDist = abs(curPos-idealPos)
                    conjLoc = curPos
                    
            if word in conj_cont:
                if abs(curPos-idealPos) < bestDist:
                    conjType = "cont"
                    bestDist = abs(curPos-idealPos)
                    conjLoc = curPos
                    
            curPos += 1
            
        #Now conj type of the centralmost conjunction is found
        #NOTE- conjLoc is its index inside the subStat- NOT stat
        ##print(conjType)
        print(conjLoc)

        sentence_polarity = 0
        if conjType == "None":
            trigrams = nltk.trigrams(stat)
            for trigram in trigrams:
                if trigram[0] in neg_words or trigram[1] in neg_words:
                   status = (status.replace(trigram[2],("NOT_"+trigram[2])))

            print(status)
            print("Trigram")
        elif conjType == "cond": #note this is not the best strategy
            #Conditional

            trigrams1 = nltk.trigrams(stat[0:conjLoc])
            trigrams2 = nltk.trigrams(stat[conjLoc:(len(stat) - 1)])

            trigrams1_neg = True in (tok in neg_words for tok in stat[0:conjLoc])
            if trigrams1_neg == True:
                for trigram in trigrams1:
                    if trigram[0] in neg_words or trigram[1] in neg_words:
                        status = (status.replace(trigram[2], ("NOT_" + trigram[2]),1))

            trigrams2_neg = True in (tok in neg_words for tok in stat[conjLoc:(len(stat) - 1)])
            if trigrams2_neg == True:
                for trigram in trigrams1:
                    if trigram[0] in neg_words or trigram[1] in neg_words:
                        status = (status.replace(trigram[2], ("NOT_" + trigram[2]),1))

            #P(S) = P(Cond, C) + P(Cons.C)
            print("Cond")

        elif conjType == "addComp":
            #Additive or Comparative type
            #P = P(RP) + P(LP)
            #assuming conjLoc is the index in stat
            trigrams1 = nltk.trigrams(stat[0:conjLoc])
            trigrams2 = nltk.trigrams(stat[conjLoc:(len(stat)-1)])

            for trigram in trigrams1:
                if trigram[0] in neg_words or trigram[1] in neg_words:
                    status = (status.replace(trigram[2], ("NOT_" + trigram[2])))


            print(status)

        elif conjType == "cont":
            #Contrasting Conjunction
            print("Cont")
            print(status)
            #if LP == NP && RP == NP
            #   P = P(RP)
            #else
            #   P = P(LP) + P(RP)
            
        
    else:
        #This status has no negation in it
        print("No Negations in Status")
        return 0
    

#negationAnalyzer(stat0)
#negationAnalyzer(stat1)
#negationAnalyzer(stat2)
#negationAnalyzer(stat3)
negationAnalyzer(stat4)
#negationAnalyzer(stat5)
negationAnalyzer(stat6)



    