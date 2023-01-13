def solution(n, s):
    if n > s :
        return [-1]
    
    answer = []
    
    for i in range(n) :
        answer.append(s//n)
        
    k = s%n
    
    for i in range(k) :
        answer[-1-i] += 1
        
    return answer