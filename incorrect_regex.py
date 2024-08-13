import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

T = int(input())
S = [input().strip() for _ in range(T)]

for exp in S:
    print(is_valid_regex(exp))
