# 수 이어 쓰기 1


# n = int(input())
n = 120
result = 0

for i in range(1, n+1):
    result += len(str(i))


print(result)

