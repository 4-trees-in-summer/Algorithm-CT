def solution(numbers, target):
    answer = 0
    
    l = len(numbers)
    def dfs(total, cnt) :        
        nonlocal answer
        
        if cnt <= l-1 :
            dfs(total+numbers[cnt], cnt+1)
            dfs(total-numbers[cnt], cnt+1)
        
        if cnt == l and total == target :
            answer += 1

    dfs(0, 0)
    
    return answer