# 가장 긴 증가하는 부분 수열
# 자신보다 작은 숫자들 중 큰 길이를 구하고 그 길이에 +1을 해준다.

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [0] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))

