from collections import defaultdict

n, m = map(int, input().split())

A = [input().strip() for _ in range(n)]
B = [input().strip() for _ in range(m)]

list_dict = defaultdict(list)

for word in B:
    if word in A:
        indices = [index + 1 for index, value in enumerate(A) if value == word]
        list_dict[word] = indices
    else:
        list_dict[word].append(-1)

for word in B:
    print(" ".join(map(str, list_dict[word])))

