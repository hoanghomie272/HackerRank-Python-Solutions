from itertools import product
K, M = map(int, input().split())
my_list = [list(map(int, input().split()))[1:] for _ in range(K)]



combi = list(product(*my_list))
modul = []
for elm in combi:
    sum_of_squares = sum(number ** 2 for number in elm)
    mod = sum_of_squares % M
    modul.append(mod)
print(max(modul))