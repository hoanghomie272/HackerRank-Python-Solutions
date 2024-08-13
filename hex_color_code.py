import re

n = int(input())
s = [input() for _ in range(n)]

pattern = r'#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})[;,)]'

for string in s:
    matches = re.findall(pattern, string)
    for match in matches:
        print(f"#{match}") 