dp = [0]*101
dp[1], dp[2], dp[3], dp[4]  = 1, 1, 1, 2,
dp[5], dp[6], dp[7], dp[8] = 2, 3, 4, 5

n = int(input())
answer = [0]*n

for i in range(n) :
  answer[i] = int(input())  

for i in range(9, max(answer)+1) :
  dp[i] = dp[i-1]+dp[i-5]

for i in answer :
  print(dp[i])