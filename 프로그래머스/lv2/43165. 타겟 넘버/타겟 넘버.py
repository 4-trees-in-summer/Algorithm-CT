def solution(numbers, target) :
    answer = 0
    l = len(numbers)
    
    def dfs(ans, idx) :
        nonlocal answer
        
        if idx == l :
            if ans == target :
                answer += 1
                return
            else :
                return
        
        dfs(ans+numbers[idx], idx+1)
        dfs(ans-numbers[idx], idx+1)
        
    dfs(0, 0)
    
    return answer