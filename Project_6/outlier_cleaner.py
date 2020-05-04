#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    x = ()
    min_error = 0
    ### your code goes here
    for i in range (len(predictions)):
        error = predictions[i]- net_worths[i]
        if error<min_error
    

    
    return cleaned_data

