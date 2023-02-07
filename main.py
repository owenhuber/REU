import matplotlib.pyplot as plt
import numpy as np

def Taurus_1d(boundary, x):
    '''places x on 1D Taurus of [- boundary, + boundary]'''
    if x < - boundary : 
        return boundary - x % (2*boundary)
    if x > boundary : 
        return x % (2*boundary) - boundary
    return x 

def x_T(T, deltaT, nu, x0, bound):
    '''for a single particle x0, with nu in taurus defined by the bound, finds position of x0 at time T with timesteps deltaT'''
    xn = x0
    for i in range(int(T/ deltaT)):
        # before converting to taurus (each step)
        not_Taurus = np.sqrt(2*nu*deltaT)*np.random.normal(0,1)
        xn += Taurus_1d(bound, not_Taurus)
        xn = Taurus_1d(bound, xn)
    return xn


def u_xt(T, deltaT, nu, dirac, bound):
    '''probability distribution of u given initial distribution dirac at time T'''
    record = []
    for val in dirac:
        x0 = val
        record.append(x_T(T, deltaT, nu, x0, bound))
    return record


def plot_at_y(arr, val, **kwargs):
    '''plotting list arr around val'''
    plt.plot(arr, np.zeros_like(arr) + val, '.', **kwargs)
    plt.show()



dirac1 = []

for i in range(100):
    dirac1.append((i%10)/200)

vals = u_xt(100, 1, .01, dirac1, 1)

plot_at_y(vals, 0)
