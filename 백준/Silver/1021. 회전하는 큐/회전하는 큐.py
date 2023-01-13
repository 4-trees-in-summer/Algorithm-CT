import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

d = deque(list(range(1, n+1)))

count = 0

for i in range(k) :
  if d.index(num[i]) <= len(d)/2 :
    for j in range(d.index(num[i])) :
      temp = d.popleft()
      d.append(temp)
      count += 1
  
  else:
    for j in range(len(d) - d.index(num[i])) :
      temp = d.pop()
      d.appendleft(temp)
      count += 1

  d.popleft()

print(count)