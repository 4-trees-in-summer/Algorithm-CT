N, K = map(int, input().split())

queue = list(range(1,N+1))

cnt = 1
i = 0

print('<', end = '')

while True :
  if cnt == N+1 :
    break
    
  elif i%K == K-1 :
    print(queue[i], end = '')
    if cnt != N :
      print(',', end =' ')
    i += 1
    cnt += 1
    
  else :
    queue.append(queue[i])
    i += 1
    
print('>')