import numpy
n, m = map(int, input().split())

my_array = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(round(numpy.std(my_array), 11))
