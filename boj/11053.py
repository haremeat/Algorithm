# 가장 긴 증가하는 부분 수열
# 자신보다 작은 숫자들 중 큰 길이를 구하고 그 길이에 +1을 해준다.

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [1] * (n + 1)

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1


print(max(dp))

