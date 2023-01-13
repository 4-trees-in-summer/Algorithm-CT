import sys

n, obj = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))
sum = []

for i in range(n-2) :
  for j in range(1, n-1) :
    for k in range(2, n) :
      if i < j < k :
        sum.append(data[i] + data[j] + data[k])

sum.sort(reverse=True)

for i in sum :
  if i <= obj :
    print(i)
    break