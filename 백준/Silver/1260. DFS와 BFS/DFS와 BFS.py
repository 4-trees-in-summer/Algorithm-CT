import sys
from collections import deque

def dfs (graph, start, visited) :
  visited[start] = True
  print(start, end = ' ')

  for i in range(1, len(graph[start])) :
    if not visited[i] and graph[start][i] == 1:
      dfs(graph, i, visited)

def bfs(graph, start, visited) :
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    print(v, end = ' ')

    for i in  range(1, len(graph[start])) :
      if not visited[i] and graph[v][i] == 1:
        queue.append(i)
        visited[i] = True
      
  
n, k, start = map(int, sys.stdin.readline().split())

visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)

graph = [[0]*(n+1) for i in range(n+1)]

for i in range(k) :
  x, y = list(map(int, sys.stdin.readline().split()))
  graph[x][y] = 1
  graph[y][x] = 1

dfs(graph, start, visited_dfs)
print()
bfs(graph, start, visited_bfs)