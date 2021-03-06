#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../Project_6/final_project_dataset.pkl", "r+b") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL')
data = featureFormat(data_dict, features)


### your code below
print(data.max())
for points in data:
    salary = points[0]
    bonus = points[1]
    matplotlib.pyplot.scatter(salary,bonus)
    
matplotlib.pyplot.xlabel('Salary')
matplotlib.pyplot.ylabel('Bonus')
matplotlib.pyplot.show()

outlier = []
for key, value in data_dict.items():
    if value['salary'] == 'NaN' or value['bonus'] == "NaN":
        continue
    elif value['salary']> 1000000 and value['bonus']>5000000:
        print(key)
        
    