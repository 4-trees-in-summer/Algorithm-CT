def solution(n, lost, reserve):
    answer = 0
    
    reserve_ = list(set(reserve) - set(lost))
    lost_ = list(set(lost)-set(reserve))
    
    reserve_.sort()
    lost_.sort()
    
    lent = 0
    for l in lost_ :
        if l-1 in reserve_ :
            lent += 1
            reserve_.remove(l-1)
        elif l+1 in reserve_ :
            lent += 1
            reserve_.remove(l+1)
            
    return n - len(lost_) + lent