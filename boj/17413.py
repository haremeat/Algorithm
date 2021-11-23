# 단어 뒤집기 2
import sys
from collections import deque

s = sys.stdin.readline().rstrip()
# s = "baekjoon online judge"

deq = deque()
stack = []

result = ''
tag = False

for i in s:
    if i == '<':
        tag = True
        deq.append(i)
        while stack:
            result += stack.pop()
    elif i == '>':
        tag = False
        deq.append(i)
        while deq:
            result += deq.popleft()
    elif i == ' ':
        if tag is True:
            deq.append(i)
            while deq:
                result += deq.popleft()
        else:
            while stack:
                result += stack.pop()
            result += ' '
    else:
        if tag is True:
            deq.append(i)
        elif tag is False and i != '>':
            stack.append(i)


while stack:
    result += stack.pop()

print(result)
