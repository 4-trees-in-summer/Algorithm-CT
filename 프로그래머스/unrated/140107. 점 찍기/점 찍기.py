import math

def solution(k, d):
    answer = d//k + 1
    i = 0
    while True :
        l = (d)**2-(i*k)**2
        
        answer += int(math.sqrt(l))//k
        i += 1
        
        if i*k > d :
            break
            
    return answer