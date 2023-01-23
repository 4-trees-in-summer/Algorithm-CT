def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1) :
        t = i//n
        idx = i%n
        
        if t == 0 :
            answer.append(idx+1)
        else :
            if idx < t+1 :
                answer.append(t+1)
            else :
                answer.append(idx+1)
        
    return answer