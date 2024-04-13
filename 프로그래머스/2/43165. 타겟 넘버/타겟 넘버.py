def solution(numbers, target):
    answer = 0
    
    def dfs(idx, cnt) :
        nonlocal answer
        
        if idx == len(numbers) :
            if target == cnt :
                answer += 1
            return
            
        
        # if idx < len(numbers) :
        dfs(idx+1, cnt + numbers[idx])
        dfs(idx+1, cnt - numbers[idx])
            
    
    dfs(0, 0)
        
        
    return answer