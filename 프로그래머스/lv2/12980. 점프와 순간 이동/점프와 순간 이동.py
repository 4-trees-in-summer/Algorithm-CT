def solution(n):
    ans = 0
    
    if n == 1 :
        return 1
    
    while True :
        if n%2 == 0 :
            n = n//2
        else :
            n = n-1
            ans += 1
        
        if n == 1 :
            return ans
        elif n == 2 :
            return ans+1
        