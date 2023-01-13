import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

data1 = sorted(set(data))

dic = {data1[i]:i for i in range(len(data1))}

for i in data :
  print(dic[i], end = ' ')