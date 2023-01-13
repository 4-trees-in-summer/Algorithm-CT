n = int(input())

table = []
sum = 0

table = list(map(int, input().split()))

table.sort()

for i in range(n) :
  for j in range(i+1) :
    sum += table[j]

print(sum)