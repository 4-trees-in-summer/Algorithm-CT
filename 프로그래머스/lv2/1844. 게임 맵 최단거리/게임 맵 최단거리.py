from collections import deque

def solution(maps):
    height = len(maps)
    width = len(maps[0])
    
    visited = [[False for _ in range(width)] for _ in range(height)]
    
    print(visited)
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def bfs(x, y) :
        nonlocal visited
        nonlocal maps
        
        q = deque([(x, y)])
        visited[x][y] = True
        
        while q :
            x, y = q.popleft()
            
            for i in range(4) :
                nx = x+dx[i]
                ny = y+dy[i]

                if 0 <= nx <= height-1 and 0 <= ny <= width-1 :
                    if visited[nx][ny] == False and maps[nx][ny] == 1 :
                        visited[nx][ny] = True
                        maps[nx][ny] = maps[x][y] + 1
                        q.append([nx, ny])
                
                else :
                    continue

                    
    bfs(0,0)

    if maps[-1][-1] == 1 :
        return -1
    else :
        return maps[-1][-1]
                