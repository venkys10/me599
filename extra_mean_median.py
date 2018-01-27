'''
def mean_filter(data, val):
    av_data = []
    for counter, i in enumerate(data):
        av_data.append(data)
        print counter, i
        for line in range(len(data)):
            val_range = range(-val / 2 + line, val / 2 + line)
            val_range_more_zero = list(filter(lambda x: x >= 0, val_range))
            count1 = len(val_range_more_zero)
            print "count1", count1
            val_range_less_list = list(filter(lambda y: y < len(data), val_range))
            count2 = len(val_range_less_list)
            print "count2", count2
            count = count1 + count2
            val = val - count
            print "count", count
            print "val", val
            data = data[((-val/2) + line) : ((val/2) + line)]
            z = sum(data)/val
            av_data.append(z)
        return av_data


#TODO do this function in a new file with function name mean_filter and two arguments

if __name__ == "__main__":
    data = generate_sensor_data()
    print mean_filter(data, 5)
    #print len(mean_filter(data, 5))

'''
'''
def mean_filter(data, val=5):
    mean_new = []
    #data = data[val:-val]

    for line in range(len(data)):

        mean_new1 = sum(data[(line+val)-(val/2) + 1: (line+val) + (val/2)])/val
        mean_new.append(mean_new1)
    #print mean_new[0]
    return mean_new
data = generate_sensor_data()
print mean_filter(data, 5)
print len(mean_filter(data, 5))
'''

'''
def value(val):
    for i in range(-val / 2, val / 2):
        count = 0
        if (val[i] >= 0) or (val[i] < len(data)):
            count = count + 1
        print count
        return count



#TODO do this function in a new file with function name mean_filter and two arguments


'''
'''
#filter width
def mean_filter_width(data, val):
    try:
        mean_width = []
        t = 0
        for line in data:
            for t in range(len(data)):
                line[t] = (sum(line[t:t-val]) + sum(line[t:t+val]))/val
                mean_width.append(line)
        return mean_width
    except val % 2 != 0 and val<0:
        print "enter an odd positive value"

data = generate_sensor_data()
print mean_filter_width(data, 5)

#width median
def median_filter(data, val):
    try:
        med_new = []
        for line in data:
            for t in range(len(data)):
                line[t] = med_new.append(line[t:t-val] + line(t: t+val))
                statistics.median(med_new)
        return med_new
    except val<0:
        print "enter positive number"

data = generate_sensor_data()
print median_filter(data, 3)

'''