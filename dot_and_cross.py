import numpy
n = int(input())

A = numpy.array([list(map(int, input().split())) for _ in range(n)])
B = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.dot(A, B))