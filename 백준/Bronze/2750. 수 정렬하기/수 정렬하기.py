data = []

n = int(input())

for i in range(n):
  x = int(input())
  data.append(x)

data.sort()

for i in range(len(data)):
  print(data[i])