# 골드바흐의 추측

import sys
import math

# num = 1000000
num = 100
prime_list = [True] * num

for i in range(1, num + 1):
    check = False
    if i > 1:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                check = True
                prime_list[i - 1] = check
        if check is False:
            prime_list[i - 1] = check

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime_list[n - i] is False:
            print("{} = {} + {}".format(n, i + 1, (n - i) - 1))
            break
        else:
            print("Goldbach's conjecture is wrong.")
