# boj 1463

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


# N이라는 수는 N // 3 을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.
# N이라는 수는 N // 2 을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.
# N이라는 수는 N-1 을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.

# 따라서 점화식은 dp[N] = min (dp[N // 3] + 1, dp[N // 2] + 1, dp[N - 1] + 1)

# 10
n = int(input())
# dp = [0 for _ in range(n+1)]  # n+1만큼의 길이를 갖는 0으로 이루어진 배열 생성
dp = [0] * (n + 1)

for i in range(2, n+1):
    dp[i] = dp[i - 1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])




# boj 2156
n = int(input())
dp = [0]
array = [0 for _ in range(n)]

# 1. 이번 포도주를 먹고 이전 포도주를 먹지 않은 경우
# 2. 이번 포도주를 먹고 이전 포도주도 먹은 경우
# 3. 이번 포도주를 먹지 않아야 하는 경우

# dp[i]는 i번째 포도주까지 최대로 마신 포도주의 양이다.

for i in range(n):
    array[i] = int(input())


dp[n] = dp[n - 1] + dp[n - 3] + array[n]
dp[n] = dp[n - 2] + array[n]
dp[n] = max(dp[n - 1] + dp[n - 3] + array[n], dp[n - 2] + array[n])