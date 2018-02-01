#!/usr/bin/env python

def gcd(a,b):
    r = a%b
    if r == 0:
        return b
    elif r == 1:
        return 1
    else:
        return gcd(b, r)

if __name__ == '__main__':
    print gcd(20,8)
