import sys

n = int(input())
data = list(map(int, sys.stdin.readline().split()))
a = data + [-1000]

for i in range(1, n+1) :
  a[i] = max(a[i], a[i]+a[i-1])

print(max(a))