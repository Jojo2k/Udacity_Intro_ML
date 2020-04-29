#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


model = GaussianNB()
t0 = time()
model.fit(features_train,labels_train)
print('training time of the classifier is ', round(time()-t0,3), 'seconds')
t1 = time()
prediction  = model.predict(features_test)
print('Prediction time of the classifier is ', round(time()-t1,3), 'seconds')
accuracy = accuracy_score(prediction,labels_test)

print('Accuracy of the naive bayes method is ', accuracy*100)
