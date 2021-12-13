# 1, 2, 3 더하기 3

import sys

t = int(sys.stdin.readline())
mod = 1000000009


def sol(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n - 1) + sol(n - 2) + sol(n - 3)


for i in range(t):
    n = int(sys.stdin.readline())
    print(sol(n) % mod)
