# 소수 찾기

# 기본적인 소수 판별 함수
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# 틀림.. why?


def check(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num + 1):
        if num % i == 0:
            return False
    return True


# 최종 제출

import sys
import math

input = sys.stdin.readline
n = int(input())

num_list = []

num_list = map(int, input().split())

prime_cnt = 0

for i in num_list:
    flag = 0
    if i > 1:
        for j in range(2, int(math.sqrt(i)) + 1):
            if (i % j == 0):
                flag += 1
        if flag == 0:
            prime_cnt += 1
print(prime_cnt)
