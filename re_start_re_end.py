import re

s = input()
k = input()

pattern = re.compile(k)

matches = []
start = 0

while True:
    match = pattern.search(s, start)
    if not match:
        break
    matches.append(match)
    
    start = match.start() + 1

if not matches:
    print("(-1, -1)")
else:
    for match in matches:
        print(f"({match.start()}, {match.end() - 1})")
