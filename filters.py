#!/usr/bin/env python

def mean_filter(a):
    with open("raw", "r+") as file_object:
        for line in file_object:
            line = ((line-1) + (line+1))/2
            print line
#TODO: do this function in a new file with function name mean_filter and two arguments
#filter width
def mean_filter_width(a, 5)

mean_filter()
