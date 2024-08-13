import numpy

n, m = map(int, input().split())
A = numpy.array([list(map(int, input().split())) for _ in range(n)])
B = numpy.array([list(map(int, input().split())) for _ in range(m)])

print(A + B)
print(A - B)
print(A * B)
print(A // B) 
print(A % B)
print(A ** B)
