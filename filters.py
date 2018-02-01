#!/usr/bin/env python

from null_filter import *
from sensor import *


def mean_filter(data, val = 3):
    av_data = []
    for j in range(len(data)):
        count = val
        sum = 0

        for i in range(-val/2, val/2):
            if (j+i >= 0) and (j + i < len(data)):
                sum = sum + data[j + i]

            else:
                count = count - 1
        z =sum/count
        av_data.append(z)

    for value, j in enumerate(av_data):
        print value, j
    return av_data


def median_filter(data, val = 3):
    av_data = []
    for j in range(len(data)):
        med_data = []

        for i in range(-val/2, val/2):
            if (j+i >= 0) and (j + i < len(data)):
                med_data.append(data[j+i])

            sorted_med = sorted(med_data)
        if len(med_data) % 2 != 0:
            av_data.append(sorted_med[len(sorted_med)/2])
        else:
            av_data.append(sorted_med[((len(sorted_med)/2 -1)+ (len(sorted_med)/2))/2])

    for enumerator, i in enumerate(av_data):
        print enumerator, i
    return av_data


if __name__ == '__main__':

    data = generate_sensor_data()
    filter_mean = mean_filter(data, 5)
    filter_median =  median_filter(data)

    print_sensor_data(data, 'raw_data')
    print_sensor_data(filter_mean, 'mean_filter')
    print_sensor_data(filter_median, 'median_filter')

    print filter_mean
    print filter_median