def solution(d, budget):
    d.sort()
    
    answer = 0
    for d_ in d :
        budget -= d_
        if budget < 0 :
            break
        answer += 1
    return answer