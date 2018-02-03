#!/usr/bin/env python

import matplotlib.pyplot as plt
import math
import numpy as np
import random

def sum_ten(iter = 10000):
    sum1 = 0
    list1 = []

    for j in range(iter):
        list2 = []
        for i in range(10):
            s = np.random.uniform(0, 1)
            list2.append(s)
            sum1 = sum(list2)
        list1.append(sum1)
    print list1
    plt.hist(list1, bins = 100)
    ax = plt.gca()
    ax.set_xlim(0,10)
    ax.set_ylim(0,500)
    plt.xlabel('sum of random distribution')
    plt.ylabel('no. of times sum value occurs')
    plt.title('Histogram_sum of list')
