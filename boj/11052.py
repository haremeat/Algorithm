# 카드 구매하기

import sys
n = int(sys.stdin.readline())
cards = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (n + 1)


dp[1] = cards[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i-j] + cards[j])

print(dp[n])

