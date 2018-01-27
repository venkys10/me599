#!/usr/bin/env python

from null_filter import *
from sensor import *


def mean_filter(data, val = 3):
    av_data = []
    new_list = []
    length = len(data)
    def mean(av_data, new_val):
        count = 0
        value = 0
        for i in new_val:
            value = value + av_data[i]
            count = count + 1
        return value/count

    val_range = range(val)
    for i in range(val):
        val_range[i] = val_range[i] - (val/2)

    for counter, i in enumerate(data):
        av_data.append(data)
        print counter, i
    for i in range(length):
        width = [x + i for x in val_range]
        count = list(filter(lambda x: x >= 0, width))
        count = list(filter(lambda y: y < length, count))
        mean_list = mean(av_data, count)
        new_list.append(mean_list)
    return new_list


def median_filter(data, val = 3):
    av_data = []
    new_list = []
    length = len(data)
    def median(av_data, new_val):
        value = []
        for i in new_val:
            value.append(av_data[i])
        value = sorted(value)
        mid = len(value)/2

        if len(value) % 2 == 0:
            return sum(value[mid-1:mid+1])/2
        else:
            return value[mid]

    val_range = range(val)
    for i in range(val):
        val_range[i] = val_range[i] - (val/2)
    for counter, i in enumerate(data):
        av_data.append(data)
        print counter, i
    for i in range(length):
        width = [x + i for x in val_range]
        count = list(filter(lambda x: x >= 0, width))
        count = list(filter(lambda y: y < length, count))
        median_list = median(av_data, count)
        new_list.append(median_list)
    return new_list



if __name__ == '__main__':
    data = generate_sensor_data()
    filter_mean = mean_filter(data, 5)
    filter_median =  median_filter(data)

    print_sensor_data(data, 'raw_data')
    print_sensor_data(filter_mean, 'mean_filter')
    print_sensor_data(filter_median, 'median_filter')

    print filter_mean
    print filter_median