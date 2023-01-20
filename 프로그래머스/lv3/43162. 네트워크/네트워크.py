def solution(n, computers):
    answer = 0
    
    visited = [False for _ in range(n)]
    
    for i in range(n) :
        if visited[i] == False :
            dfs(i, n, computers, visited)
            answer += 1
            
    return answer

def dfs(num, n, computers, visited) :
    if visited[num] == True :
        return
    
    visited[num] = True
    
    for i in range(n) :
        if i != num and computers[num][i] == 1 :
            dfs(i, n, computers, visited)
        elif i == n-1 and computers[num][i] == 0 :
            return
    
    