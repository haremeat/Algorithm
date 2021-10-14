
# 거스름 돈
n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)


# 첫째 줄에 N과 K가 공백을 기준으로 하여 각각 자연수로 주어집니다.
# 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력합니다.
n, k = map(int, input().split())
count = 0

# // 버림 나눗셈. 실수가 나오며 소수점 이하는 버린다.

while True:
    target = (n // k) * k
    count += (n - target)
    n = target

    if n < k:
        break

    count += 1
    n //= k

count += (n - 1)
print(count)


# 곱하기 혹은 더하기
S = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(S[0])

for i in range(1, len(S)):
    num = int(S[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)





