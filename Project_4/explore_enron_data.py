#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np

enron_data = pickle.load(open(r"E:\GitHub\Udacity_Intro_ML\Project_4\final_project_dataset.pkl", "rb"))

count= 0
for name,value in enron_data.items():
    if  value['total_payments'] == 'NaN':
        count+=1



# Multiple questions were answered bby changing the parameters of dictionary.