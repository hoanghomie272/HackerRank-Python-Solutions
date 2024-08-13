def check_strict_superset(A, B):
    if all(elm in A for elm in B) and any(elm not in B for elm in A):
        return True
    else:
        return False

A = set(input().split())
n = int(input())
count = 0

for _ in range(n):
    B = set(input().split())
    if check_strict_superset(A, B):
        count += 1

if count == n:
    print("True")
else:
    print("False")