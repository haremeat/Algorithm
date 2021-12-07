# 가장 긴 증가하는 부분 수열

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [1] * (n + 1)

for i in range(n + 1):
    for j in range(i):
        if a[j] < a[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1


print(dp[n])

