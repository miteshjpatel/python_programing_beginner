# Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)
print("Peoples age: ", ages)
print("Percentile meaning 75% of the people are younger then ", numpy.percentile(ages,75))
print("Percentile meaning 85% of the people are younger then ", numpy.percentile(ages,85))
print("Percentile meaning 95% of the people are younger then ", numpy.percentile(ages,95))
print("Percentile meaning 100% of the people are younger then ", numpy.percentile(ages,100))
