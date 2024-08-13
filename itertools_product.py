from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [A, B]
output = ' '.join(f"({', '.join(map(str, elm))})" for elm in product(*C))

print(output)  