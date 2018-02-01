#!/usr/bin/env python

#sum using for loop
def sum_i(l):
    list_prev = 0
    for i in l:
        new_list = i + list_prev
        list_prev = new_list
    return list_prev

#sum using recursion
def sum_r(l):
    if len(l) == 0:
        return False
    else:
        return l[0] + sum_r(l[1:])

if __name__ == '__main__':

    print sum_i([6,2,3,4])
    print sum_r([1,2,3,4])