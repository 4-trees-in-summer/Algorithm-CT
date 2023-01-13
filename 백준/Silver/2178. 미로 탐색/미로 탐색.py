from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
map = []

for i in range(n) :
  map.append(list(input()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y) :
  queue =deque()
  map[y][x] = '0'
  distance = 1
  queue.append((y,x, distance))

  while queue :
    y, x, distance = queue.popleft()
      
    for i in range(4) :
      n_y = int(y) + dy[i]
      n_x = int(x) + dx[i]

      if 0 <= n_y < n and 0 <= n_x < k :
        if n_y == n-1 and n_x == k-1 :
          return distance+1
        elif map[n_y][n_x] == '1' :
          map[n_y][n_x] = '0'
          queue.append((n_y, n_x, distance + 1))

  return distance
  
print(bfs(0, 0))