n = 3
#####

dp = [0] * 1001
dp[0], dp[1], dp[2] = 0, 1, 3

for i in range(3, n+1):
    dp[i] = dp[i-1] + 2*dp[i-2]

print(dp[n]%796796)