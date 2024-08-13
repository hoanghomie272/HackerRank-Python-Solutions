n, m = map(int, input().split())
arr = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

total_happiness = 0

for number in arr:
    if number in A:
        total_happiness += 1
    if number in B:
        total_happiness -= 1

print(total_happiness) 

