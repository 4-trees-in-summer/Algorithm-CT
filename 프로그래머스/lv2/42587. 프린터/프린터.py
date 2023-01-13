def solution(p, location):
    cnt = 0
    p1 = sorted(p, reverse=True)
    
    print(p1)
    
    while True :
        if p[0] == p1[0]:
            cnt += 1
            
            if location == 0 :
                break
            else :
                location -= 1
                
            p.pop(0)
            p1.pop(0)
            
        else :
            temp = p.pop(0)
            p.append(temp)
            
            if location == 0 :
                location += len(p)-1
            else :
                location -= 1
    
    return cnt