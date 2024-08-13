N, X = map(int, input().split())
my_list = [list(map(float, input().split())) for _ in range(X)]

new_list = zip(*my_list)

for marks in new_list:
    print(sum(marks)/len(marks))