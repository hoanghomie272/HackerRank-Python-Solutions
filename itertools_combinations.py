from itertools import combinations
S, k =  input().split()
k = int(k)
S = ''.join(sorted(S))
for i in range(1, k + 1):
    for elm in list(combinations(S, i)):
        print(''.join(sorted(elm)))