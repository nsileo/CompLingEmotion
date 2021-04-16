import sklearn as skl
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import sklearn.metrics as metrics
import numpy as np
import random


#generate preditions for nrclex with emoticons (nrclex_emo)
data = pd.read_csv('continuous_outcome_base.csv',
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

#split data LOO

class_error_ext = list()
class_error_opn = list()
class_error_agr = list()
class_error_con = list()
class_error_neu = list()
i = 0
for user in set(data["#AUTHID"]):
    print(i/2.5, " %")
    i+=1
    #test_users = random.sample(set(data.iloc[:,1]), 1)
    #print(test_users)
    data_test = data[data["#AUTHID"] == user]
    data_test = data_test.iloc[:, 2:17]
    covariates_test =  data_test.iloc[:,6:14]
    #print(len(covariates_test))



    data_train = data[data["#AUTHID"] != user ]
    data_train = data_train.iloc[:,2:17]
    covariates =  data_train.iloc[:,6:14]
    #print(covariates.head())
    #print(len(covariates))
    #covariates[covariates==0] = 0.1



    rf_reg_e= LogisticRegression()
    rf_reg_e.fit(covariates,data_train['sEXT'])

    mean_score = 1*(np.mean(rf_reg_e.predict(covariates_test))>=0.5)
    print(rf_reg_e.predict(covariates_test), data_test['sEXT'] )
    class_error_ext.append(mean_score == np.mean(data_test['sEXT']))

    rf_reg_o = LogisticRegression()
    rf_reg_o.fit(covariates,data_train['sOPN'])

    mean_score = 1 * (np.mean(rf_reg_o.predict(covariates_test)) >= 0.5)

    class_error_opn.append(mean_score == np.mean(data_test['sOPN']))



    rf_reg_a =  LogisticRegression()
    rf_reg_a.fit(covariates,data_train['sAGR'])

    mean_score = 1 * (np.mean(rf_reg_a.predict(covariates_test)) >= 0.5)

    class_error_agr.append(mean_score == np.mean(data_test['sAGR']))

    rf_reg_c = LogisticRegression()
    rf_reg_c.fit(covariates,data_train['sCON'])

    mean_score = 1 * (np.mean(rf_reg_c.predict(covariates_test)) >= 0.5)

    class_error_con.append(mean_score == np.mean(data_test['sCON']))

    rf_reg_n = LogisticRegression()
    rf_reg_n.fit(covariates,data_train['sNEU'])


    mean_score = 1 * (np.mean(rf_reg_n.predict(covariates_test)) >= 0.5)

    class_error_neu.append(mean_score == np.mean(data_test['sNEU']))
print('Class. Error Rates for NRCLex base: ')
print('EXT: ', 1-np.mean(class_error_ext))
print('OPN: ',1-np.mean(class_error_opn))
print('AGR: ',1-np.mean(class_error_agr))
print('CON: ',1-np.mean(class_error_con))
print('NEU: ', 1-np.mean(class_error_neu))
results_emo_lem = pd.DataFrame(zip(class_error_ext,class_error_con, class_error_agr,class_error_con,class_error_neu))
results_emo_lem.to_csv('results_base_logreg.csv')