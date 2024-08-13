import numpy

def arrays(arr):
    reversed_list = arr[::-1]
    return numpy.array(reversed_list, float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)