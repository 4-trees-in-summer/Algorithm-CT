N = int(input())

dp = [0]*(N+1)
for num in range(3, N+1) :
    if num%3 == 0 :
        dp[num] = num//3
    if num%5 == 0 :
        dp[num] = num//5

    if dp[num-3] != 0 :
        dp[num] = dp[num-3] + 1
    if dp[num-5] != 0 :
        dp[num] = dp[num-5] + 1

if dp[N] == 0 :
    print(-1)
else :
    print(dp[N])