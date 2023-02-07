import matplotlib.pyplot as plt
import numpy as np
import math
from Taurus1d import * 



# HEAT EQUATION ON 1D TAURUS

# simulating different initial distributions
dirac1 = []
for i in range(10000):
    dirac1.append((i%10)/20000)


# our list of positions at T = 100 with time steps of 1, on the Taurus bounded by [-1, 1] 
vals_1d = u_xt(100, 1, .01, dirac1, 1)


# plotting our findings in 1D
hist1d(vals_1d, 0.005)
# plot_1d(vals_1d, 0)

# For our example list, percentage of trajectories ending up in x>0
print(prob(0, 1, vals_1d))