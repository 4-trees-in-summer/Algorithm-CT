n, k = map(int, input().split())

coins = []
sum = 0

for i in range(n) :
  coins.append(int(input())) 

for i in range(n) :
  num = k//coins[n-1-i]
  sum += num

  k -= coins[n-1-i]*num

print(sum)
  