#  Standard deviation is a number that describes how spread out the values are.
#  A low standard deviation means that most of the numbers are close to the mean (average) value.
#  A high standard deviation means that the values are spread out over a wider range.
#  Example: This time we have registered the speed of 7 cars:


import numpy

speed = [86,87,88,86,87,85,86]
speed2 = [32,111,138,28,59,77,97]
speed3 = [32,111,138,28,59,77,97]


print("Standard Diviation of speed ", speed, ": ", numpy.std(speed))
print("Standard Diviation of speed ", speed2, ": ", numpy.std(speed2))
print("Variance of speed ", speed2, ": ", numpy.var(speed2))

