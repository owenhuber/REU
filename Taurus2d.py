import matplotlib.pyplot as plt
import numpy as np
import math
from math import log
from Taurus1d import *

# Helper function working on the Taurus in 1D

def Taurus_2d(boundary, x):
    '''places [x, y] on 2D Taurus of [- boundary, + boundary] X [- boundary, + boundary]'''
    return [Taurus_1d(boundary, x[0]), Taurus_1d(boundary, x[1])]


# For Simulating the heat equation on 1D Taurus

def x_T2(T, dt, nu, x0, bound):
    '''for a single particle x0, with nu in taurus defined by the bound, finds position of x0 at time T with timesteps deltaT'''
    xn = x0
    for i in range(int(T/ dt)):
        # before converting to taurus (each step)
        not_Taurus1 = np.sqrt(2*nu*dt)*np.random.normal(0,1)
        not_Taurus2 = np.sqrt(2*nu*dt)*np.random.normal(0,1)
        temp = Taurus_2d(bound, [not_Taurus1, not_Taurus2])
        xn[0] += temp[0]
        xn[1] += temp[1]
        xn = Taurus_2d(bound, xn)
    return xn


def u_xt2(T, dt, nu, dirac, bound):
    '''probability distribution of u given initial distribution dirac at time T'''
    record = []
    for val in dirac:
        x0 = val
        record.append(x_T2(T, dt, nu, x0, bound))
    return record


# for integrating

def prob(a, b, lis) : 
    '''approximate of probability that a random value of the list 'lis' is between a and b'''
    c = min(a, b)
    d = max(a, b)
    i = 0
    lis.sort()
    # the count we wish to return
    ret = 0
    s = len(lis)
    while i < s and a > lis[i] : 
        i+= 1
    while i < s and lis[i] <= b:
        i += 1
        ret += 1
    return ret/s


# Functions for plotting in 1D

def plot_2d(arr):
    '''plotting list arr around val'''
    zip(*arr)
    plt.scatter(*zip(*arr), s = 1/4)
    plt.show()


def hist2d(lis, binSize):
    bins = np.arange(-1, 1, binSize) # fixed bin size
    plt.xlim([min(lis)-1, max(lis)+1])
    plt.hist(lis, bins=bins, alpha=0.5)
    plt.title('dostribution after T')
    plt.xlabel('x')
    plt.ylabel('probability * 100')
    plt.show()