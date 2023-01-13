import sys
from collections import deque

sum_w = 0
sum_b = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]
 
n_x, n_y = map(int, sys.stdin.readline().split())
war = []

visited = [[False]*(n_x) for i in range(n_y)]

for i in range(n_y):
  war.append(input())

def bfs(y, x, team) :
  #queue = deque([[x,y]])
  queue =deque()
  queue.append((y,x))
  visited[y][x] = True
  
  count = 1

  while queue :
    y, x = queue.popleft()
    
    for i in range(4):
      new_x = x+dx[i]
      new_y = y+dy[i]
      
      if (0 <= new_y < n_y ) and (0 <= new_x < n_x):
        '''
        print(y,x)
        print(visited[y][x])
        if visited[y][x] :
          print('a')
        elif not visitied[y][x] :
          print('b')
        '''
        if war[new_y][new_x] == team and not visited[new_y][new_x]:
          queue.append((new_y, new_x))
          visited[new_y][new_x] = True
          count += 1
  
    
  return count
          
for i in range(n_y) :
  for j in range(n_x) :
    if not visited[i][j] :
      cnt = bfs(i, j, war[i][j])

      if war[i][j] == 'W' :
        sum_w += cnt**2
      else :
        sum_b += cnt**2

print(sum_w, sum_b)