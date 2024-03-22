def solution(arr):
    answer = []
    
    for idx, a in enumerate(arr) :
        if idx == 0 :
            answer.append(a)
            temp = a
            continue
        
        if temp == a :
            continue
        
        answer.append(a)
        temp = a
        
    return answer