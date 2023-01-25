def solution(numbers, target):
    answer = 0
    
    def dfs(idx, sum_) :
        if idx == len(numbers) :
            nonlocal answer
            if sum_ == target :
                answer += 1
            return
        
        else :
            dfs(idx+1, sum_+numbers[idx])
            dfs(idx+1, sum_-numbers[idx])
    
    dfs(0, 0)
    
    return answer