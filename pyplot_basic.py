#!/usr/bin/env python

import matplotlib.pyplot as plt
import math
import numpy as np

def sin_curve():
    t = np.arange(0.0, 4*np.pi, 0.1)
    s = np.sin(t)
    plt.plot(t, s, lw=2)
    ax = plt.gca()
    ax.set_xlim(0,4*np.pi)
    ax.set_ylim(-1,1)
    plt.title('A sin curve')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
