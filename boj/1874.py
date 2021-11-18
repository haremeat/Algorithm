# 스택 수열

# pop()이 나와야 하는 조건 : stack[-1]값이 target과 같다
# current가 target값과 작거나 같을 때까지는 계속 더해준다. +
# 이 모든 과정이 끝났을 때 stack이 비어있지 않으면 NO를 출력한다.


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
    print("\n".join(answer))
else:
    print("NO")

# 위는 오답
