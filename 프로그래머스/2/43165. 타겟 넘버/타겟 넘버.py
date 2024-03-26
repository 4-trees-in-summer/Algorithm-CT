def solution(numbers, target):
    answer = 0
    
    def dfs(depth, cnt) :
        if depth == len(numbers) :
            if cnt == target :
                nonlocal answer
                answer += 1
            return
        
        dfs(depth+1, cnt+numbers[depth])
        dfs(depth+1, cnt-numbers[depth])
    
    dfs(0, 0)
    return answer