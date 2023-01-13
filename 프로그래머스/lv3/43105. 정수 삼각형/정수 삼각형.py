def solution(triangle):
    l = len(triangle)
    dp = [[] for _ in range(l)]
    
    k = -1
    for i in triangle :
        k += 1
        for j in i :
            dp[k].append(j)

    for i in range(1, len(dp)) :
        for j in range(len(dp[i])) :
            if j-1 < 0 :
                dp[i][j] += dp[i-1][j]
            elif j == len(dp[i]) -1 :
                dp[i][j] += dp[i-1][j-1]
            else :
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
    
    return max(dp[len(triangle)-1])