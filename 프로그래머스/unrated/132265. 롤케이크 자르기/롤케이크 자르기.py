from collections import Counter

def solution(topping):
    answer = 0
    
    cnt = Counter(topping)
    l = len(cnt)
    brother = set()
    t = True
    for i in topping :
        brother.add(i)
        cnt[i] -= 1
        
        if cnt[i] == 0 :
            cnt.pop(i)
        if len(brother) > len(cnt) :
            if t == True :
                return 0
            else :
                break
                
        if len(cnt) == len(brother) :
            answer += 1
            t = False
        
        
    
    return answer

                
    