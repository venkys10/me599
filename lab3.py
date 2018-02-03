#!/usr/bin/env python

from times import *
from MassSpringDamper import *
from sum_iter import *
from pyplot_basic import *


if __name__ == '__main__':
    #Question 2: Sin_curve
    sin_curve()
    plt.show()

    # Question 3: Histogram
    sum_ten(10000)
    plt.show()
    # Question 4: displacement, time graph
    plot_msd()


    # Question 5: times
    time_sum()
    plt.show()
    time_sort()
    plt.show()
