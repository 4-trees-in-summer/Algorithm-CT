def solution(n, works):
    if sum(works) <= n :
        return 0
    
    works.sort(reverse=True)
    print(works)
    idx = 1 
    while n>0:
        if idx == len(works)-1 :
            while n > 0 :
                for i in range(len(works)) :
                    if n == 0 :
                        break
                    works[i] -= 1
                    n -= 1
            
        if works[idx-1] <= works[idx] :
            idx += 1
            continue
            
        for i in range(idx) :
            if n == 0 :
                break
            works[i] -= 1
            n -= 1
            
    answer = 0
    for i in works :
        answer += i**2
        
    return answer