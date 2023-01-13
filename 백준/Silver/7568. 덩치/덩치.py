from operator import itemgetter, attrgetter

n = int(input())
data = []

for i in range(n) :
  data.append(list(map(int, input().split())))
  
count = []

for i in range(n) :
  cnt = 1
  for j in range(n) :
   if data[i][0] < data[j][0] and data[i][1] < data[j][1] :
      cnt += 1

  count.append(cnt)

for i in count :
  print(i, end = ' ')