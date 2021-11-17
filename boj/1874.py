# 스택 수열
import sys
input = sys.stdin.readline

# n = int(input())
# targets = [int(input()) for _ in range(n)]

n = 8
targets = [4, 3, 6, 8, 7, 5, 2, 1]

current = 1
stack = []
answer = []

for target in targets:
    while current <= target:
        stack.append(current)
        answer.append("+")
        current += 1

    if stack[-1] == target:
        answer.append("-")
        stack.pop()


if not stack:
    for i in answer:
        print(i)
else:
    print("No")

# 위는 오답



