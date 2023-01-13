import sys

n,m = map(int, input().split())

N = set()
M = set()

for i in range(n) :
  N.add(input())

for j in range(m) :
  M.add(input())

if n < m :
  print(len(M - (M-N)))
  
  for i in sorted(M - (M-N)):
    print(i)

else :
  print(len(N - (N-M)))
  
  for i in sorted(N - (N-M)):
    print(i)  
  