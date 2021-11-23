# 쇠막대기

import sys
s = list(sys.stdin.readline().rstrip())
# s = "(((()(()()))(())()))(()())"
stack = []
result = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    elif s[i] == ')':
        stack.pop()
        if s[i - 1] == '(':
            # 레이저
            result += len(stack)
        else:
            # 쇠막대기의 끝
            result += 1

print(result)
