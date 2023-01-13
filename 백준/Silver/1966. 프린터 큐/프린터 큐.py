from collections import deque

num = int(input())

for i in range(num):
  n, k = map(int, input().split())
  # n은 전체 len
  # k는 원하는 index
  importance = deque(list(map(int, input().split())))

  count = 0
  i = 0

  for i in range(n) :
    h = max(importance)
    # importance에서 가장 큰 값
    index_h = importance.index(h)
    # importance에서 가장 가장 큰 값의 '수'

    if index_h == k :
      count += 1
      break
    
    else :
      if index_h > k :
        #k = (n-1) - (index_h - k)
        k = k - (index_h) + (len(importance) - 1)
        
      elif index_h < k :
        k = k - (index_h + 1)
        
      for i in range(index_h) :
        importance.append(importance[0])
        importance.popleft()
        
      importance.popleft()
      count += 1

  print(count)