import numpy

P = numpy.array(list(map(float, input().split())))
x = float(input()) 

print(numpy.polyval(P, x))