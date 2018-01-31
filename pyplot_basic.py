#!/usr/bin/env python

import matplotlib.pyplot as plt
import math
import numpy as np

t = np.arange(0.0, 12.0, 0.1)
s = np.sin(4*np.pi*t)
plt.plot(t, s, lw = 2)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()