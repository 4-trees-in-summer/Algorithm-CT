def solution(n, s):
    if n > s :
        return [-1]
    
    answer = [0 for _ in range(n)]
    
    for i in range(n) :
        answer[i] = s//n
        
    if sum(answer) == s :
        return answer
    elif sum(answer) < s :
        idx = -1
        for i in range(s-sum(answer)) :
            answer[idx] += 1
            idx -= 1
            
        return answer