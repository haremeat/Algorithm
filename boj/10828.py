# 스택

# input() 함수를 사용할 경우 시간초과가 뜬다.
# sys.stdin.readline > raw_input() > input()
# n = int(input())

import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])