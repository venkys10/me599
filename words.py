#!/usr/bin/env python


def letter_count(a,b):
    count = 0
    for letters in a:
        if letters.lower() in b.lower():
            count = count+1
    return count


print "The number of times letter repeats is ", letter_count('halLway', 'l')
