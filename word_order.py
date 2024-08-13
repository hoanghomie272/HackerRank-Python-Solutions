from collections import Counter

n = int(input())
word = [input() for _ in range(n)]

counter = Counter(word)

print(len(set(word)))
print(" ".join(str(value) for key, value in counter.items()))