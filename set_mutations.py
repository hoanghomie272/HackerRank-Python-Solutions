n = int(input())
A = set(map(int, input().split()))
m = int(input())

for _ in range(m):
    cmd = input().split()
    B = set(map(int, input().split()))
    if cmd[0] == "intersection_update":
        A.intersection_update(B)
    if cmd[0] == "update":
        A.update(B)
    if cmd[0] == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    if cmd[0] == "difference_update":
        A.difference_update(B)

print(sum(A))

