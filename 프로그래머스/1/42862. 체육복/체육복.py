def solution(n, lost, reserve):
    answer = 0
    
    lost_ = list(set(lost) - set(reserve))
    reserve_ = list(set(reserve) - set(lost))
    already_reserved = []
    
    for l in lost_ :
        for r in reserve_ :
            if r in already_reserved :
                continue
            
            if abs(r-l) <= 1 :
                already_reserved.append(r)
                break
    
    return n - len(lost_) + len(already_reserved)