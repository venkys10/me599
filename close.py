#!/usr/bin/env python

def close(a, b, c):
    if abs(a - b) < c:
        print(True)
    else:
        print(False)

close(1,2,3)