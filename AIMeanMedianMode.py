#   Mean - The average value
#   Median - The mid point value
#    Mode - The most common value

import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)
print("Mean speed: ", x)

x = numpy.median(speed)
print("Median speed: ", x)

y = stats.mode(speed)
print(y)

