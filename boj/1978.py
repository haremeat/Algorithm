# 소수 찾기

# 틀림.. why?

n = int(input())
sosu = list(map(int, input().split()))
count = 0

def check(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2,num+1):
        if num % i == 0:
            return False
    return True

for i in sosu:
    if check(i):
        count += 1

print(count)

