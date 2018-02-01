#!/usr/bin/env python
import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
def estimate_pi():
    sum_c = 0
    k = 0
    const = (2 * math.sqrt(2)) / 9801
    while True:
        num = ((factorial(4*k))*(1103 + 26390*k))
        den  = ((factorial(k)**4)*(396**(4*k)))
        exp = const*(num/den)
        sum_c = sum_c + exp

        if abs(exp) < 1e-15:
            break
        else:
            k = k + 1

    return 1/sum_c
if __name__ == '__main__':

    print estimate_pi()
    print math.pi