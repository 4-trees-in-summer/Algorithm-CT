from collections import deque

def solution(maps):
    answer = []
    island = maps
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    def bfs(days,visited,q) :
        while q:
            x,y = q.popleft()
            if not visited[x][y] :
                days += int(island[x][y])
                visited[x][y] = True
            else :
                continue
            
            for i in range(4) :
                ax, ay = x+dx[i], y+dy[i]
                if -1 < ax < len(maps) and -1 < ay < len(maps[0]) and not visited[ax][ay] and island[ax][ay] != 'X' :
                    q.append([ax, ay])
        
        answer.append(days)
                        
    
    for x in range(len(maps)) :
        for y in range(len(maps[0])) :
            if not visited[x][y] and island[x][y] != 'X':
                q = deque()
                q.append([x,y])
                bfs(0, visited, q)
    
    answer.sort()
    return answer if answer else [-1]