#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    # prediction a list of predictions 
    # ages is the list of ages of people
    # net worth is the target value
    # 90 elements in each list
    import numpy as np
    cleaned_data = []
    error = np.array(net_worths-predictions)
    
    for i in range(81):
        pos = np.argmin(error)
        tup = (ages[pos],net_worths[pos],error[pos])
        cleaned_data.append(tup)
        error = np.delete(error, pos)
    # for iter_num in range(len(error)-1,0,-1):
    #     for idx in range(iter_num):
    #         if error[idx]>error[idx+1]:
    #             temp1 = error[idx]
    #             error[idx] = error[idx+1]
    #             error[idx+1] = temp1
                
    #             temp3 = ages[idx]
    #             ages[idx] = ages[idx+1]
    #             ages[idx+1] = temp3
                
    #             temp3 = net_worths[idx]
    #             net_worths[idx] = net_worths[idx+1]
    #             net_worths[idx+1] = temp3
    
    # for i in range(81):
    #     tup =(ages[:i],net_worths[:i],error[:i]) 
    #     cleaned_data.append(tup)
    
    return cleaned_data