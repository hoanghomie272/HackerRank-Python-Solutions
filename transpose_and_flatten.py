import numpy
n, m = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(n)]

arr = numpy.array(lst)
print(arr.transpose())
print(arr.flatten())


