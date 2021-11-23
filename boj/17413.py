# 단어 뒤집기 2
import sys
from collections import deque

# s = sys.stdin.readline().rstrip()
s = "<ab cd>ef gh<ij kl>"

deq = deque()
stack = []

result = ''
tag = False

for i in s:
    if i == '<':
        tag = True
        deq.append(i)
        while len(deq) == 0:
            result += deq.popleft()
    elif i == '>':
        tag = False
        deq.append(i)
        while len(deq) == 0:
            result += deq.popleft()
    else:
        if tag is True:
            deq.append(i)
            while len(deq) == 0:
                result += deq.popleft()
        elif tag is False and i != '>':
            stack.append(i)



print(deq)
