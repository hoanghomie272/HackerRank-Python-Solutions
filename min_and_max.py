import numpy
n, m = map(int, input().split())

my_array = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.max(numpy.min(my_array, axis = 1)))