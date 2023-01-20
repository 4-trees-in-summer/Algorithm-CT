from itertools import combinations

def solution(nums):
    answer = 0
    
    numbers = combinations(nums, 3)
    
    for i in numbers :
        if sosu(sum(i)) :
            answer += 1
        
    return answer

def sosu(n) :
    cnt = 0
    
    for i in range(1, n+1) :
        if n%i == 0 :
            cnt += 1
    
    if cnt == 2:
        return True
    else :
        return False