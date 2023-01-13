def solution(n):
    dp = [0 for _ in range(n+1)]
    
    dp[1] = 1
    dp[2] = 1
    
    if n <= 2 :
        return dp[n]
    
    k = 3
    while k <= n :
        dp[k] = dp[k-1] + dp[k-2]
        k += 1
        
    return dp[n]%1234567