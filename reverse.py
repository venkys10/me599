#!/usr/bin/env python


#recursive reverse
def reverse_r(l):
    if len(l) == 0:
        return l
    else:
        return [l[-1]] + reverse_r(l[:-1])
        #return reverse_r(l[1:]) + [l[0]]

def reverse_normal(l):
    size = len(l)
    iter = size/2
    index = size - 1
    for i in xrange(0, iter):
        temp = l[index]
        l[index] = l[i]
        l[i] = temp
        index = index - 1
    return l

if __name__ == "__main__":
    print reverse_normal([1,2,3,4,5])

    print reverse_r([1,2,3,4])
