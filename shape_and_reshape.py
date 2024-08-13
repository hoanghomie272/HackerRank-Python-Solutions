import numpy
lst = list(map(int, input().split()))
arr = numpy.array(lst)

print(numpy.reshape(arr, (3, 3)))