# Program that calculates mean, median and mode in python
import numpy
import statistics
n =int(input("Enter the index of the list:"))
x = list()
print ("Enter the elements in the list:")
for i in range(n):
    num = input()
    x.append(int(num))
mean = numpy.mean(x)
median = numpy.median(x)
mode = statistics.mode(x)
print ("The mean is: ",mean)
print ("The median is: ",median)
print ("The mode is: ",mode)