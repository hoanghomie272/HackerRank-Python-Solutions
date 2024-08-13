from itertools import groupby

S = input()

grouped = groupby(S)

result = [(len(list(group)), int(key)) for key, group in grouped]

print(" ".join(f"({count}, {key})" for count, key in result))