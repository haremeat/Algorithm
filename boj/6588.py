# 골드바흐의 추측

import sys
import math

n = int(sys.stdin.readline())
num_list = map(int, sys.stdin.readline().split())

prime_cnt = 0

for i in num_list:
    check = False
    if i > 1:
        for j in range(2, int(math.sqrt(i)) + 1):
            if (i % j == 0):
                check = True
        if check is False:
            prime_cnt += 1
print(prime_cnt)
