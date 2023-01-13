import sys

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

count = 0


for i in data:
  abc = []
  
  if len(i) == 1:
    count += 1
    continue
    
  for j in range(len(i)) :
    if j == 0 :
      k = i[j]
      abc.append(k)
    else :
      if i[j] != k :
        if i[j] not in abc :
          abc.append(k)
          k = i[j]
        else :
          count -= 1
          break

  count += 1
  
print(count)