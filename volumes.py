#!/usr/bin/env python

import math

def cylinder_volume(r, h):
    if r>0 and h>0:
        vol = math.pi*(r*r)*h
        print(vol)
    else:
        print(None)

def torus_vol(r, R):
    if r>0 and R>0:
        vol = (math.pi*r*r)*(2*math.pi*R)
        print(vol)
    else:
        print(None)


if __name__ == '__main__':
    print ('cylinder_volume = '),cylinder_volume(3,4)
    print ('torus_volume  = '),torus_vol(3,4)