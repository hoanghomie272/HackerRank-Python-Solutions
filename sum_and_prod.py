import numpy
n, m = map(int, input().split())

my_array = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.prod(numpy.sum(my_array, axis = 0)))