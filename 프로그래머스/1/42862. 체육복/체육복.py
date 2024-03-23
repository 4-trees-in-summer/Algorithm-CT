def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    
    reserved = 0
    lost_ = list(set(lost)-set(reserve))
    reserve_ = list(set(reserve)-set(lost))

    for l in lost_ :
        for r in reserve_ :
            if abs(r-l) <= 1 :
                reserved += 1
                reserve_.remove(r)
                break
    
    return n - len(lost_) + reserved