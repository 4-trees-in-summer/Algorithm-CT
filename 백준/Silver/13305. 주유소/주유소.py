n = int(input())

dist = list(map(int, input().split()))
city = list(map(int, input().split()))

x = 0
pay = 0 

for i in range(n-1) :
  if city[i] > city[i+1] :
    pay += city[i-x]*dist[i]
    x = 0
  else :
    pay += city[i-x]*dist[i]
    x += 1

print(pay)
    