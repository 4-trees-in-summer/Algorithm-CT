n = int(input())
data = []


for i in range(n) :
  cnt = 0
  x = input()
  
  for j in x :
    if j == '(' :
       cnt += 1
    elif j == ')' :
      if cnt == 0:
        cnt = 100
        continue
      else :
        cnt -= 1

  if cnt == 0 :
    print('YES')
  else :
    print('NO')
  