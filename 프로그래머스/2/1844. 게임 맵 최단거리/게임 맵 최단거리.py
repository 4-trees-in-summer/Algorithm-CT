from collections import deque

def solution(maps):
    answer = 0
    
    d_r = [1, -1 ,0, 0]
    d_c = [0, 0, 1, -1]
    
    max_r = len(maps)
    max_c = len(maps[0])
    
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    q = deque()
    q.append([0, 0, 1])
    
    while q :
        r, c, cnt = q.popleft()
        
        if [r, c] == [max_r-1, max_c-1] :
            return cnt
        
        for d_r_, d_c_ in zip(d_r, d_c) :
            r_ = r + d_r_
            c_ = c + d_c_
            
            if 0 <= r_ < max_r and 0 <= c_ < max_c and maps[r_][c_] == 1 and not visited[r_][c_]:
                q.append([r_, c_, cnt+1])
                visited[r_][c_] = True
            
            
    return -1