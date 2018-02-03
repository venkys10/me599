import matplotlib.pyplot as plt
import matplotlib
import math
import numpy as np
import random
from scipy.integrate import odeint
from numpy import arange
import time


l1 = [1, 10, 100, 1000, 10000, 100000, 1000000]

def time_sum():
    time_all1 = []
    
    for i in range(len(l1)):
        list_new1 = []
        for j in range(l1[i]):
            myrandom = random.random()
            list_new1.append(myrandom)
        start = time.clock()
        sum(list_new1)
        elapsed_sum = (time.clock() - start)
        time_all1.append(elapsed_sum)

    x1 = np.arange(len(l1))
    axes = plt.gca()
    axes.set_ylim([0.0, 0.008])
    plt.yticks(np.arange(0.0, 0.009, 0.002))
    plt.xticks(x1, l1)
    plt.bar(x1, time_all1, .5, align='center', alpha=0.5)
    plt.title('Summation time')
    plt.ylabel('Time')
    plt.xlabel('Length of list')
    plt.show()



def time_sort():
    time_all2 = []
    for i in range(len(l1)):
        list_new2 = []
        for j in range(l1[i]):
            myrandom2 = random.random()
            list_new2.append(myrandom2)
        start = time.clock()
        sorted(list_new2)
        elapsed_sort = (time.clock() - start)
        time_all2.append(elapsed_sort)
    

    plt.plot(time_all2, l1)
    y1 = np.arange(len(l1))
    axes = plt.gca()
    axes.set_ylim([0.0, 0.6])
    plt.yticks(np.arange(0.0, 0.7, 0.1))
    plt.xticks(y1, l1)
    plt.bar(y1, time_all2, .5, align='center', alpha=0.5)
    plt.title('Sorting time')
    plt.ylabel('Time')
    plt.xlabel('Length of list')
    plt.show()
