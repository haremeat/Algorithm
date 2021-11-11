# 분해합

# n = 216

n = int(input())
result = 0
temp = 0

for i in range(1, n + 1):
    temp = sum(map(int, str(i)))
    result = i + temp
    if result == n:
        print(i)
        break
else:
    print(0)