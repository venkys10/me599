#!/usr/bin/env python

#from times import *
#from MassSpringDamper import *
from sum_iter import *
from pyplot_basic import *

#TODO check 3, 4, 5

if __name__ == '__main__':
    #Question 2: Sin_curve
    sin_curve()

    # Question 3: Histogram
    sum_ten(10000)
    plt.show()
'''
    # Question 4: displacement, time graph
    smd = MassSpringDamper(m = 10.0, k = 10.0, c = 1.0)
    state, t = smd.simulate(0.0, 1.0)
    plt.show()

    # Question 5: times
    time_sum()
    plt.show()
    time_sort()
    plt.show()
'''