# boj 1463

x = int(input())

dp = [0, 0, 1, 1]

for i in range(4, x + 1):
    dp.append(dp[i - 1] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[x])

# N이라는 수는 N // 3 을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.
# N이라는 수는 N // 2 을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.
# N이라는 수는 N-1 을 연산전으로 돌리면, 즉 +1을 하면 만들 수 있다.

# 따라서 점화식은 dp[N] = min (dp[N // 3] + 1, dp[N // 2] + 1, dp[N - 1] + 1)

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
dp = [0] * n
wine = [int(input()) for _ in range(n)]

dp[0] = wine[0]

if n > 1:
    dp[1] = wine[0] + wine[1]

if n > 2:
    dp[2] = max(wine[2] + wine[0], wine[2] + wine[1], dp[1])

for i in range(3, n):
    # 마지막 잔을 마시지 않을 경우도 넣어야 한다.
    dp[i] = max(wine[i] + dp[i - 2], wine[i] + wine[i - 1] + dp[i - 3], dp[i - 1])

print(dp[n - 1])


dp[n] = dp[n - 1] + dp[n - 3] + wine[n]
dp[n] = dp[n - 2] + wine[n]
dp[n] = max(dp[n - 1] + dp[n - 3] + wine[n], dp[n - 2] + wine[n])



# 개미전사

n = int(input())

# 모든 식량정보
array = list(map(int, input().split()))

dp = [0] * 100

# bottom-up
dp[0] = array[0]
dp[1] = max(array[0], array[1])

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i])

print(dp[n - 1])

