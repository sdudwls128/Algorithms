# Algorithms_Greedy_01

n = int(input())
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n//coin
    n %= coin

print(coin)