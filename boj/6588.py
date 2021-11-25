# 골드바흐의 추측
# 아무리 바꿔봐도 시간초과를 피할 수가 없네

import sys
import math

num = 1000001
prime_list = [True] * num

for i in range(1, num):
    check = False
    if i > 1:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                check = True
                prime_list[i] = check
        if check is False:
            prime_list[i] = check

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    for i in range(2, (n // 2) + 1):
        if prime_list[n - i] is False:
            print("{} = {} + {}".format(n, i, n - i))
            break
