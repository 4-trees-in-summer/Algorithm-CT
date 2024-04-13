from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [False for _ in range(len(computers))]
    
    for idx, computer in enumerate(computers) :
        if not visited[idx] :
            answer += 1
            visited[idx] = True
        
        q = deque()
        q.append(idx)
        
        while q :
            idx = q.popleft()

            for idx_, com in enumerate(computers[idx]) :
                if idx_ == idx or visited[idx_] or com == 0 :
                    continue
                    
                q.append(idx_)
                visited[idx_] = True
    
    return answer