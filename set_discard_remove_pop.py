n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    cmd = input().split()
    if cmd[0] == "pop" and len(s) > 0:
        s.pop() 
    elif cmd[0] == "remove" and int(cmd[1]) in s:
        s.remove(int(cmd[1]))
    elif cmd[0] == "discard":
        s.discard(int(cmd[1]))

print(sum(s))