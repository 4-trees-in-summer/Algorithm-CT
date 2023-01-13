def solution(m, n, puddles):
    answer = 0
    
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for j,i in puddles :
        dp[i][j] = -1
    
    dp[1][1] = 1
        
    for i in range(1,m+1) :
        for j in range(1, n+1) :
            if dp[j][i] == -1 :
                continue
            elif dp[j][i-1] == -1 and dp[j-1][i] != -1 :
                dp[j][i] += dp[j-1][i]
            elif dp[j][i-1] != -1 and dp[j-1][i] == -1 :
                dp[j][i] += dp[j][i-1]
            elif dp[j][i-1] == -1 and dp[j-1][i] == -1 :
                continue
            else :
                dp[j][i] += dp[j-1][i] + dp[j][i-1]

    
    return dp[-1][-1]%1000000007