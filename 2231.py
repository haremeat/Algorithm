# 분해합

n = 216

# n = int(input())

result = 0


for i in range(1, 1000001):
    for j in str(i):
        i += int(j)
        if i == n:
            result = j


print(result)