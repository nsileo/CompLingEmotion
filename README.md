# CompLingEmotion
CompLing Group Project

In the NRCLex package, you will find 4 nrclex_ files. Each file is a extra improvement ot nrclex base. 

To create a dataset with of the improvements, refer to the sentiment_score_ file with chosen improvemnt. 
For example, sentiment_score_emo_lem.py creates a dataset with NRC Lex with emoticons and lemmatization based on mypersonality_final.csv .

Then, you can either use prediction_ to create Random Forest models with the selected version of the nrclex packag.
Alternatively, choose log_ to fit Logistic Regression. There is also svm_emo_lem.py which utilizes SVM with rbf. 
It takes a considerable amount of time to run.

You will also find an R script which was used to analyze the results of the emoticon survey.
All results were saved to csv files and named accordingly. 
