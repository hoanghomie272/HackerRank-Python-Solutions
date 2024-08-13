from collections import defaultdict

K = int(input())
rooms = list(map(int, input().split()))

count_dict = defaultdict(int)

for room in rooms:
    count_dict[room] += 1

for room, count in count_dict.items():
    if count == 1:
        print(room)
        break