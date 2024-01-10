from collections import deque

def bfs(num, computers, visited, answer) :
    q = deque()
    q.append(num)
    
    while q :
        computer = q.popleft()
        visited[computer] = True
        
        for idx, link in enumerate(computers[computer]) :
            if not visited[idx] and link == 1 :
                q.append(idx)
    
    return answer+1, visited

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for num in range(n) :
        if not visited[num] :
            answer, visited = bfs(num, computers, visited, answer)
        
    return answer