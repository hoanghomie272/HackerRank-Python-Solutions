from collections import Counter

X = int(input())
N = list(map(int, input().split()))
x = int(input())

shoe_counter = Counter(N)

total_money = 0

for _ in range(x):
    size, price = map(int, input().split())
    if shoe_counter[size] > 0:
        total_money += price
        shoe_counter[size] -= 1

print(total_money)
