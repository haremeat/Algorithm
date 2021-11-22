# 요세푸스 문제

import collections
import sys

# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())

n = 7
m = 3
data = []

for i in range(n):
    data.append(i)

deq = collections.deque(data)
result = []


for i in range(n):
    for j in range(m):
        deq.append(deq[0])
        deq.pop()
        if j % m == 0:
            result.append(deq[-1])




