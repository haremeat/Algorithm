# 2×n 타일링

import sys

n = int(sys.stdin.readline())

dp = [1] * (n + 1)
result = 0

if n == 1:
    result = 1
else:
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    result = dp[n] % 10007

print(result)

