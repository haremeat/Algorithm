# 숨바꼭질 6

import sys
from math import gcd

n, s = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
result = 0
distance = []

for i in range(n):
    distance.append(abs(s - int(a[i])))

# print(gcd(48, 24, 24))
for i in range(len(distance)):
    result = gcd(distance[i], result)

print(result)
