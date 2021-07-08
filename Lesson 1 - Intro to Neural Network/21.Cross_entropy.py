import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    result = 0
    for i in range(len(Y)):
        result -= np.sum(Y[i] * np.log(P[i]) + (1 - Y[i]) * np.log(1 - P[i]))
    return result
    #or:
    #Y = np.float_(Y)
    #P = np.float_(P)
    #return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
    #result = 0
