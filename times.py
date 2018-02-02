import matplotlib.pyplot as plt
import math
import numpy as np
import random
from scipy.integrate import odeint
from numpy import arange


def time_sum():
    l1 = [1, 10, 100, 1000, 10000, 100000, 1000000]
    time_all1 = []
    for i in l1:
        myrandom = random.sample(range(1000000), l1[i])
        start = time.clock()
        sum(myrandom)
        elapsed_sum = (time.clock() - start)
        time_all1.append(elapsed_sum)
    #return time_all1
    plt.title('Time_summation')
    plt.xlabel('Time')
    plt.ylabel('Length of list')
    plt.plot(time_all1, l1)

def time_sort():
    l2 = [1, 10, 100, 1000, 10000, 100000, 1000000]
    time_all2 = []
    for i in l2:
        myrandom = random.sample(range(1000000), l2[i])
        start = time.clock()
        sorted(myrandom)
        elapsed_sort = (time.clock - start)
        time_all2.append(elapsed_sort)
    #return time_all2
    plt.title('Time_sorting')
    plt.xlabel('Time')
    plt.ylabel('Length of list')
    plt.plot(time_all2, l2)

#TODO check if working