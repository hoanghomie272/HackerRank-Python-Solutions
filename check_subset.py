def check_subset(A, B):
    if all(elm in B for elm in A):
        print("True")
    else:
        print("False")

T = int(input())

for _ in range(T):
    m = int(input())
    A = set(input().split())
    n = int(input())
    B = set(input().split())
    check_subset(A, B)

