def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for r in range(1, n+1) :
        for c in range(1, m+1) :
            ## puddle 일때
            if [c, r] in puddles :
                continue
            
            if [r, c] == [1,1] :
                dp[r][c] = 1
                continue
            
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    
    
    return dp[n][m]%1000000007