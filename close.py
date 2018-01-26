#!/usr/bin/env python

def close(a, b, c):
    if abs(a - b) < c:
        return True
    else:
        return False


print close(1,2,0.5)