M = int(input())
arr_1 = set(map(int, input().split()))
N = int(input())
arr_2 = set(map(int, input().split()))

for number in sorted(arr_1.difference(arr_2).union(arr_2.difference(arr_1))):
    print(number)
