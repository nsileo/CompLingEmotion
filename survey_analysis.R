rm(list=ls())
data = read.csv('/Users/dyngs/Downloads/Computational Linguistics_March 30, 2021_15.03.csv')
emotis = list(":D",":)",":P","<3","</3","xD",":((","xd","^.^","0.o",":))",":|",
         ":/",";D",":*",":3","0.0",":$",":p",":pp")
library(hash)
answers = hash()

for (emoti in emotis){
  answers[[paste(emoti,"_positive")]]=list()
  answers[[paste(emoti,"_negative")]]=list()
  answers[[paste(emoti,"_joy")]]=list()
  answers[[paste(emoti,"_sadness")]]=list()
  answers[[paste(emoti,"_fear")]]=list()
  answers[[paste(emoti,"_disgust")]]=list()
  answers[[paste(emoti,"_surprise")]]=list()
  answers[[paste(emoti,"_anticipation")]]=list()
  
}
positive = list()
negative = list()
joy = list()
sadness = list()
fear = list()
disgust = list()
surprise = list()
anticipation = list()

for (emoti in emotis){
  emo1 = data[data$P1.1 == emoti| data$P2.1 ==emoti | data$P3.1 ==emoti
            | data$P4.1 ==emoti | data$P5.1 ==emoti| data$P6.1 ==emoti ,]
  emo1=emo1[,18:length(names(emo1))]
  indicies = list(2,11,20,29,38,47)
  
  for (i in indicies){
    for (j in 1:nrow(emo1[i])){
     
      if (emo1[j,i] == emoti){
        
        answers[[paste(emoti,"_positive")]]=append(answers[[paste(emoti,"_positive")]],emo1[j,i-1])
        answers[[paste(emoti,"_negative")]]=append(answers[[paste(emoti,"_negative")]],emo1[j,i+1])
        
        answers[[paste(emoti,"_joy")]]=append(answers[[paste(emoti,"_joy")]],emo1[j,i+2])
        
        answers[[paste(emoti,"_sadness")]]=append(answers[[paste(emoti,"_sadness")]],emo1[j,i+3])
        
        answers[[paste(emoti,"_fear")]]=append(answers[[paste(emoti,"_fear")]],emo1[j,i+4])
        
        answers[[paste(emoti,"_disgust")]]=append(answers[[paste(emoti,"_disgust")]],emo1[j,i+5])
        
        answers[[paste(emoti,"_surprise")]]=append(answers[[paste(emoti,"_surprise")]],emo1[j,i+6])
        
        answers[[paste(emoti,"_anticipation")]]=append(answers[[paste(emoti,"_anticipation")]],emo1[j,i+7])

      }
    }
  
  }

}
#hashmap where each emotion has 8 proportion tests (1 for each sentiment)
confidence_interval = hash()

for (emoti in emotis){
  positive = answers[[paste(emoti,"_positive")]]
  negative =answers[[paste(emoti,"_negative")]]
  joy=answers[[paste(emoti,"_joy")]]
  sadness =answers[[paste(emoti,"_sadness")]]
  fear = answers[[paste(emoti,"_fear")]]
  disgust =  answers[[paste(emoti,"_disgust")]]
  surprise =answers[[paste(emoti,"_surprise")]]
  anticipation = answers[[paste(emoti,"_anticipation")]]
  
  positive = as.numeric(positive)
  negative= as.numeric(negative)
  joy= as.numeric(joy)
  sadness= as.numeric(sadness)
  fear = as.numeric(fear)
  disgust= as.numeric(disgust)
  surprise = as.numeric(surprise)
  anticipation= as.numeric(anticipation)
  
  emotions=list(positive,negative,joy,sadness,fear,
                disgust,surprise,anticipation)
  j=0
  for (emotion in emotions){
    j= j+1
    count_success = 0
    for (i in 1:length(emotion)){
      if (emotion[i] <= 2) {
        count_success = count_success + 1 
      }
    }
    print(emoti)
    print(count_success)
    conf_int = binom.test(count_success,length(emotion),p = 0.5,alternative="greater")
    confidence_interval[[paste(emoti, j)]] = conf_int
  }
}
emoti_emotion = list()
conf_int_upper = list()
conf_int_lower = list()
p_value = list()
for (key in keys(confidence_interval)){
  value = confidence_interval[[key]]
  emoti_emotion = append(emoti_emotion,key)
  conf_int_upper = append(conf_int_upper,value$conf.int[2])
  conf_int_lower = append(conf_int_lower,value$conf.int[1])
  p_value = append(p_value,value$p.value)
  print(key)
  print(value$conf.int[1:2])
  
}

results = cbind(emoti_emotion,p_value)
print(results)
write.csv(cbind(emoti_emotion,p_value),
          '/Users/dyngs/Desktop/results_pvalues.csv')

