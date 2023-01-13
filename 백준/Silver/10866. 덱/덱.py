import sys
from collections import deque

n = int(input())

deque = deque([])

for i in range(n) :
  word = sys.stdin.readline().split()

  if word[0] == 'push_front' :
    deque.appendleft(word[1])

  elif word[0] == 'push_back' :
    deque.append(word[1])

  elif word[0] == 'pop_front' :
    if len(deque) == 0 :
      print(-1)
    else: 
      print(deque.popleft())

  elif word[0] == 'pop_back' :
    if len(deque) == 0 :
      print(-1)
    else: 
      print(deque.pop())
    
  elif word[0] == 'size' :
    print(len(deque))
    
  elif word[0] == 'empty' :
    if len(deque) == 0 :
      print(1)
    else :
      print(0)

  elif word[0] == 'front' :
    if len(deque) == 0 :
      print(-1)
    else :
      print(deque[0])
      
  elif word[0] == 'back' :
    if len(deque) == 0 :
      print(-1)
    else:
      print(deque[-1])