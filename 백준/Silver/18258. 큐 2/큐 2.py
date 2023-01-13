import sys

n = int(sys.stdin.readline())
queue = []

cnt = 0

for i in range(n) :
  x = sys.stdin.readline().split()

  if x[0] == 'push' :
    queue.append(x[1])
    
  elif x[0] == 'pop' :
    if len(queue) > cnt :
      print(queue[cnt])
      cnt += 1
    else :
      print(-1)
      
  elif x[0] == 'size' :
    print(len(queue) - cnt)
    
  elif x[0] == 'empty' :
    if len(queue) == cnt :
      print(1)
    else :
      print(0)
      
  elif x[0] == 'front' :
    if len(queue) > cnt :
      print(queue[cnt])
    else :
      print(-1)
      
  elif x[0] == 'back' :
    if len(queue) > cnt :
      print(queue[-1])
    else :
      print(-1)
  