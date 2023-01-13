def solution(s):
    answer = True
    
    cnt1 = 0
    cnt2 = 0
    for i in s :
        if i in 'pP' :
            cnt1 += 1
        elif i in 'yY' :
            cnt2 += 1
            

    if cnt1 == cnt2 :
        return True
    else :
        return False