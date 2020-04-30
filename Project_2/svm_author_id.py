#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

#########################################################

# features_train = features_train[:int(len(features_train)/100)]
# labels_train = labels_train[:int(len(labels_train)/100)]

model = SVC(kernel = 'rbf', C = 100)
t0 = time()
model.fit(features_train, labels_train)
print('training time of the classifier is ', round(time()-t0,3), 'seconds')

t1 = time()
prediction = model.predict(features_test)
print('Prediction time of the classifier is ', round(time()-t1,3), 'seconds')


accuracy = accuracy_score(prediction, labels_test)
print('Accuracy of the svm method is ', accuracy*100)

