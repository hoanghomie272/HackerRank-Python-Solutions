n = int(input())
english = input().split()
b = int(input())
french = input().split()

s = set(english)
print(len(s.symmetric_difference(french)))