import operator

n = int(input())
data = []

for i in range(n) :
  data.append(list(map(int, input().split())))

data = sorted(data)
data = sorted(data, key = operator.itemgetter(1))

time_cur = [0, -1]
count = 0

for i in data :
  if i[0] >= time_cur[1] :
    count += 1
    time_cur = i

print(count)