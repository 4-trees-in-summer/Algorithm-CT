from collections import deque

def solution(n, computers):
    answer = 0
    visited = []
    
    for n_ in range(n) :
        if n_ in visited :
            continue
            
        q = deque([n_])

        while q : 
            idx = q.popleft()
            visited.append(idx)
            
            for idx_, computer in enumerate(computers[idx]) :
                if idx_ not in visited and computer == 1:
                    q.append(idx_)
        
        if visited == list(range(n)) :
            answer += 1
            break
        else :
            answer += 1
                
    return answer