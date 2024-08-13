from collections import OrderedDict

N = int(input())
ordered_dict = OrderedDict()

for _ in range(N):
    item_name, net_price = input().rsplit(maxsplit=1)
    if item_name in ordered_dict:
        ordered_dict[item_name] += int(net_price)
    else:
        ordered_dict[item_name] = int(net_price)

for item_name, total_price in ordered_dict.items():
    print(f"{item_name} {total_price}")
