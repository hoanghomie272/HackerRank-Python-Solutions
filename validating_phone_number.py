import re

n = int(input())
phone_numbers = [input() for _ in range(n)]

pattern = r'^[789]{1}\d{9}$'

for phone_number in phone_numbers:
    if re.match(pattern, phone_number):
        print("YES")
    else:
        print("NO")


