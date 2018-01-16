#!/usr/bin/env python

import math

def torus_vol(r, R):
    vol = (math.pi*r*r)*(2*math.pi*R)
    print(vol)


torus_vol(3, 4)