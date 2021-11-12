# 소수 찾기

# 기본적인 소수 판별 함수
# def is_prime_number(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True


# 틀림.. why?



# def check(num):
#     if num == 1:
#         return False
#     elif num == 2:
#         return True
#     for i in range(2, num + 1):
#         if num % i == 0:
#             return False
#     return True

# 에라토스테네스의 체
import math

n = int(input())
sosu = list(map(int, input().split()))

def is_prime_number(num, arr):
    flag = 0
    count = 0

    for i in arr:
        if i > 1:
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    flag += 1
            if flag == 0:
                count += 1

    return count


print(is_prime_number(n, sosu))

# 틀림..