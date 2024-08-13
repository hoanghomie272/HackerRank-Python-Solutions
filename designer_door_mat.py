N, M = map(int, input().split())
txt = ".|."
for i in range(N // 2):
    print((txt*(2*i + 1)).center(M, "-"))
print("WELCOME".center(M, "-"))
for i in range(N // 2):
    print((txt*(N - 2 - 2*i)).center(M, "-"))   
    