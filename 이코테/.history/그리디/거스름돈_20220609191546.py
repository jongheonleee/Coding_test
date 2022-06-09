'''
In: 거스름돈(n) = 1260
Out: 거슬러 줘야할 동전의 최소 개수(cnt)
'''

# idea : 가장 큰 단위의 화폐부터 최대한 많이 거슬러 준다.

n = 1260
cnt = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    cnt += n // coin
    n %= coin

print(cnt)
