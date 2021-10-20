# 백준 1463

# x = int(input())
#
# dp = [0, 0, 1, 1]
#
# for i in range(4, x + 1):
#     dp.append(dp[i - 1] + 1)
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i // 3] + 1)
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i // 2] + 1)
#
# print(dp[x])


# 백준 2156
n = int(input())
dp = []
array = []

dp[n] = dp[n - 1] + dp[n - 3] + array[n]
dp[n] = dp[n - 2] + array[n]

dp[n] = max()





