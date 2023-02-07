import matplotlib.pyplot as plt
import numpy as np
import math
from Taurus1d import * 
from Taurus2d import *
from math import log
import random


##########################################################################################################################################
# HEAT EQUATION ON 1D TAURUS

# simulating different initial distributions
dirac1 = []
for i in range(10000):
    dirac1.append((i%10)/20000)


# our list of positions at T = 100 with time steps of 1, on the Taurus bounded by [-1, 1] 
vals_1d = u_xt1(100, 1, .01, dirac1, 1)


# plotting our findings in 1D

hist1d(vals_1d, 0.005)
plot_1d(vals_1d, 0)

# For our example list, percentage of trajectories ending up in x>0

print(prob(0, 1, vals_1d))


#########################################################################################################################################
# HEAT EQUATION ON 2D TAURUS

# simulating different initial distributions
dirac2 = []
for i in range(10000):
    dirac2.append([(i%10)/2000, random.randint(1, 10)/ 2000])


# our list of positions at T = 100 with time steps of 1, on the Taurus bounded by [-1, 1] X [-1, 1]
vals_2d = u_xt2(100, 1, 0.00001, dirac2, 1)


# Plotting our findings in 2D
plot_2d(vals_2d)

