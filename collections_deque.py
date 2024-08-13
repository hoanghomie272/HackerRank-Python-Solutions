from collections import deque
N = int(input())
d = deque()

for _ in range(N):
    method = input().split()
    if method[0] == "append":
        d.append(method[1])
    if method[0] == "appendleft":
        d.appendleft(method[1])
    if method[0] == "pop":
        d.pop()
    if method[0] == "popleft":
        d.popleft()

print(" ".join(d))
