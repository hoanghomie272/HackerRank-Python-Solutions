from itertools import combinations_with_replacement
S, k = map(str, input().split())
k = int(k)
for elm in combinations_with_replacement(sorted(S), k):
    print("".join(letter for letter in elm))