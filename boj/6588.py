# 골드바흐의 추측

import sys
import math

num = 1000000
prime_list = [True] * num

for i in range(2, int(math.sqrt(num)) + 1):
    if prime_list[i] is True:
        for j in range(i * 2, num, i):
            if prime_list[j] is True:
                prime_list[j] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    for i in range(3, num):
        if prime_list[i] is True:
            if prime_list[n - i] is True:
                print("{} = {} + {}".format(n, i, n - i))
                break
