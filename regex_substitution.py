import re

n = int(input())
s = [input() for _ in range(n)]

def replace_patterns(string):
    replace_1 = re.sub(r'(?<= )&&(?= )', 'and', string)
    replace_2 = re.sub(r'(?<= )\|\|(?= )', 'or', replace_1)
    return replace_2

replaced_strings = [replace_patterns(string) for string in s]

print('\n'.join(replaced_strings))
