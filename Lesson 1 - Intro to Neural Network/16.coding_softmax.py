import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    exponents = np.exp(L)
    sumExp = np.sum(exponents) #a scalar
    result = []
    for i in exponents:
        result.append(i*1.0/sumExp)
    return result
    
    # Note: The function np.divide can also be used here, as follows:
    # def softmax(L):
    #     expL = np.exp(L)
    #     return np.divide (expL, expL.sum())
