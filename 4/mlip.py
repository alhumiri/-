import sys

import numpy as np

import matplotlib.pyplot as plt

sys.path.append('..')



# Cost function. 
# Computes the cost for using theta as the parameter for 
# the linear regression for fitting the data in x and y.

def cost_function(x, y, theta):
    m = len(y)
    cost = np.sum(np.square(x.dot(theta) - y))
    return (1 / (2*m)) * cost


def gradient_descent(x, y, theta, alpha, iters):
    m = len(y)
    cost = np.zeros(iters)
    theta = theta.copy()
    
    for i in range(iters):
        error = x.dot(theta) - y
        theta = theta - (alpha/m) * error.dot(x)
        cost[i] = cost_function(x, y, theta)              
    return theta, cost
    
# Since the sizes in sq feets are much larger than 
# the number of bedrooms we need to normalize.

def feature_normalize(x):
    """
    Here x is the m x n feature matrix. Normalizing
    the features would involve subtracting their 
    respective means from the dataset and dividing by
    thei respective standard deviations.
    """
    x = x.copy()
    mu = np.average(x, axis=0) # mean of each column
    sigma = np.std(x, axis=0) # standard deviation of each column
    x = (x - mu) / sigma
    return x, mu, sigma


