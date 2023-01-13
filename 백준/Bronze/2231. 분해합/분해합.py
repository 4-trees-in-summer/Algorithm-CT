n = int(input())
answer = n
data = []
  
for i in range(n,1,-1) :
  sum = n
  
  n = str(n)
  for i in range(len(n)) :
    sum += int(n[i])

  n = int(n)
  if sum == answer :
    data.append(n)
    n -= 1
  else :
    n -= 1

data.sort()
if len(data) == 0 :
  print(0)
else :
  print(data[0])
    
  