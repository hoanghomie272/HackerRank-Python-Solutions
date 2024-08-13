from itertools import combinations

n = int(input())
my_list = input().split()
k = int(input())

combi = list(combinations(my_list, k))
count = 0
for elm in combi:
    if "a" in elm:
        count += 1

print(count/len(combi))
