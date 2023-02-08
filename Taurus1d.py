import matplotlib.pyplot as plt
import numpy as np
import math

# Helper function working on the Taurus in 1D

def Taurus_1d(boundary, x):
    '''places x on 1D Taurus of [- boundary, + boundary]'''
    if x < - boundary : 
        return boundary - x % (2*boundary)
    if x > boundary : 
        return x % (2*boundary) - boundary
    return x 


# For Simulating the heat equation on 1D Taurus

def x_T1(T, dt, nu, x0, bound):
    '''for a single particle x0, with nu in taurus defined by the bound, finds position of x0 at time T with timesteps deltaT'''
    xn = x0
    for i in range(int(T/ dt)):
        # before converting to taurus (each step)
        not_Taurus = np.sqrt(2*nu*dt)*np.random.normal(0,1)
        xn += Taurus_1d(bound, not_Taurus)
        xn = Taurus_1d(bound, xn)
    return xn

def RK2_T1(T, dt, x_p, x0, h):
    '''Using RK2 for approximations, in progress'''
    current = x0
    tracking = [x0]
    for i in range(0, int(T/dt)):
        
        F1 = dt*x_p(current, dt*i)
        F2 = dt*x_p(current + F1/2, dt*i + dt/2)
        
        current += F2 
        tracking.append(current)
    return tracking

def u_xt1(T, dt, nu, dirac, bound):
    '''probability distribution of u given initial distribution dirac at time T'''
    record = []
    for val in dirac:
        x0 = val
        record.append(x_T1(T, dt, nu, x0, bound))
    return record


# for integrating

def prob1d(a, b, lis) : 
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

def plot_1d(arr, val, **kwargs):
    '''plotting list arr around val'''
    plt.plot(arr, np.zeros_like(arr) + val, '.', **kwargs)
    plt.show()

def hist1d(lis, binSize):
    bins = np.arange(-1, 1, binSize) # fixed bin size
    plt.xlim([min(lis)-1, max(lis)+1])
    plt.hist(lis, bins=bins, alpha=0.5)
    plt.title('distribution after T')
    plt.xlabel('x')
    plt.ylabel('Relative Prob')
    plt.show()