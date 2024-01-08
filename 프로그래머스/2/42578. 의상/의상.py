def solution(clothes):
    answer = 1
    
    cnt = {}
    for cloth in clothes :
        if cloth[1] not in cnt.keys() :
            cnt[cloth[1]] = 1
        else :
            cnt[cloth[1]] += 1
    
    cnt_values = cnt.values()

    for c in cnt_values :
        answer *= c+1
        
    return answer - 1