from itertools import permutations
S, k =  input().split()
k = int(k)
S = ''.join(sorted(S))
for elm in list(permutations(S, k)):
    print(''.join((elm)))