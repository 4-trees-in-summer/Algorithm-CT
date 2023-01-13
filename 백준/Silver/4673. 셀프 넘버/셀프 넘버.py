num = list(range(1, 10001))
self_num = set()

for i in num :
  sum = i
  for j in str(i) :
    sum += int(j)
  
  self_num.add(sum)

num = set(num)

for i in sorted(num-self_num) :
  print(i)