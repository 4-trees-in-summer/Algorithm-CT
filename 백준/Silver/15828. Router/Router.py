n = int(input())

queue = []
cnt = 0

while True :
  x = int(input())

  if x == 0 :
    cnt += 1
    
  elif x == -1:
    break

  else :
    queue.append(x)   

for i in range(cnt, len(queue)) :
  print(queue[i], end = ' ')
