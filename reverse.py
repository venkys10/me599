#!/usr/bin/env python


#recursive reverse
def reverse_r(l):
    if len(l) == 0:
        return l
    else:
        print l
        return [l[-1]] + reverse_r(l[:-1])
        #return reverse_r(l[1:]) + [l[0]]

print reverse_r([1,2,3,4])
