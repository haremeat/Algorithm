# 요세푸스 문제

from collections import deque
# import sys

n, m = map(int, input().split())

deq = deque()

for i in range(1, n + 1):
    deq.append(i)

result = []

for i in range(n):
    for j in range(m):
        if j == m - 1 and deq:
            result.append(deq.popleft())
        elif j < m - 1 and deq:
            f = deq.popleft()
            deq.append(f)

# print(result)

print("<" + ", ".join(map(str, result)) + ">")
