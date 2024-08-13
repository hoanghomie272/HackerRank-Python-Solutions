import numpy

n = int(input())
A = numpy.array([list(map(float, input().split())) for _ in range(n)])

print(round(numpy.linalg.det(A), 2))