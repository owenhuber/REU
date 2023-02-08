import matplotlib.pyplot as plt
import numpy as np
import math
from Taurus1d import * 
from Taurus2d import *
from math import log
import random
import imageio


##########################################################################################################################################
# HEAT EQUATION ON 1D TAURUS

# # simulating different initial distributions
# dirac1 = []
# for i in range(10000):
#     dirac1.append(0)


# # our list of positions at T = 100 with time steps of 1, on the Taurus bounded by [-1, 1] 
# vals_1d = u_xt1(100, 1, .0001, dirac1, 1)


# # plotting our findings in 1D

# hist1d(vals_1d, 0.01, 1)
# plot_1d(vals_1d, 0)

# For our example list, percentage of trajectories ending up in x>0

# print(prob1d(0, 1, vals_1d))


#########################################################################################################################################
# # HEAT EQUATION ON 2D TAURUS

# simulating different initial distributions
dirac2 = []
for i in range(20):
    for j in range(500):
        # uncomment below for inintial weight at origin
        # dirac2.append([(i%10)/2000, random.randint(1, 10)/ 2000])
        # uncomment below for initial weight in lines across y axis
        dirac2.append([(i - 10)/10,(j - 250)/250])


# our list of positions at T = 100 with time steps of 1, on the Taurus bounded by [-1, 1] X [-1, 1]
vals_2d = u_xt2(1, 0.1, 0.000001, dirac2, 1)

for i in range(1, 10):
    plot_2d(u_xt2(i/10, 0.1, 0.00001, dirac2, 1))


# Plotting our findings in 2D

# plot_2d(vals_2d)



# # for plotting 3d concentration map ()
# dic = {}

# for i in range(200):
#     for j in range(200):
#         if i == 100 and j == 100: 
#             dic[('%.2f' % 0) + ('%.2f' % 0)] = 0
#         elif i == 100: 
#             dic[('%.2f' % 0) + ('%.2f' % ((-100 + j)/100))] = 0
#         elif j == 100: 
#             dic[('%.2f' % ((-100 + i)/100)) + ('%.2f' % 0)] = 0
#         else : 
#             dic[('%.2f' % ((-100 + i)/100)) + ('%.2f' % ((-100 + j)/100 ))] = 0

# for val in vals_2d : 
#     n = val[0]
#     m = val[1]
#     if round(n, 2) == 0 :
#         n = '%.2f' % 0
#     else : 
#         n = '%.2f' % val[0]
#     if round(m, 2) == 0:
#         m = '%.2f' % 0
#     else : 
#         m = '%.2f' % val[1]
#     try :    
#         dic[n + m] += 1
#     except : 
#         print(f'{n + m}')


# # grouping by weights of bins
# weights = []
# #index
# k = 0

# # getting our concentrations
# for i in range(200):
#     for j in range(200):
#         weights.append([(-100 + i)/100, (-100 + j)/100, list(dic.values())[k]])
#         k += 1


# def Heat_3d(lis):
#     x, y, dz = zip(*weights)
#     for i in range(len(dz)) : 
#         val = dz[i]
#         dz[i] = val/10000
    
#     plt.rcParams["figure.figsize"] = [7.50, 3.50]
#     plt.rcParams["figure.autolayout"] = True

#     fig = plt.figure()

#     ax1 = fig.add_subplot(111, projection='3d')

#     dx = np.ones(40000)/100
#     dy = np.ones(40000)/100
#     z = np.zeros(40000)

#     ax1.bar3d(x, y, z, dx, dy, dz, color="red")
#     ax1.axis('off')
#     plt.show()

#     plt.show()



# # print(weights)
# # Heat_3d(weights)

# # print(prob2d(-0.05, 0.05, -0.05, 0.05, weights))