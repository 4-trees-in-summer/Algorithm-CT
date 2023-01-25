def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1) :
        idx = i//n
        if idx == 0 :
            answer.append(i+1)
        elif idx > 0 :
            if i%n <= idx :
                answer.append(idx+1)
            elif i%n > idx :
                answer.append(i%n + 1)
            
    return answer