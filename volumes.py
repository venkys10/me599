#!/usr/bin/env python

import math

def cylinder_volume(r, h):
    if r>0 and h>0:
        vol_c = math.pi*(r**2)*h
        return vol_c
    else:
        return None
    
def torus_vol(R, r):
    if R>0 and r>0:
        vol_t = (2*math.pi*R)*(math.pi*(r**2))
        return vol_t
    else:
        return None

if __name__ == '__main__':
    print ('cylinder_volume = '),cylinder_volume(3,4)
    print ('torus_volume = '),torus_vol(4,-3)