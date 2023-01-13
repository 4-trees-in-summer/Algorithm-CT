import sys

n, k = map(int, sys.stdin.readline().split())
n = int(n)
k = int(k)

data_digit = {}
data_alpha = {}

for i in range(1, n+1) :
  d = sys.stdin.readline().rstrip()
  data_digit[str(i)] = d
  data_alpha[d] = str(i)

for i in range(k) :
  ans = sys.stdin.readline().rstrip()
  
  if ans.isalpha() :
    print(data_alpha[ans])
  elif ans.isdigit() :
    print(data_digit[ans])  