# 오큰수
# 틀린 이유 : 인접하지 않은 오큰수를 얻는 경우의 수를 계산하지 않음
# 일단 예시 케이스 2개는 성공 -> 내일 와서 정답 맞춰보기

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1] * n

for i in range(n):
    stack.append(i)
    if i < n - 1 and arr[i] < arr[i + 1]:
        stack.pop()
        result[i] = arr[i + 1]

        if stack and arr[stack[-1]] < arr[i + 1]:
            result[stack[-1]] = arr[i + 1]
            stack.pop()

# 스택 값이 남아있다면
if stack:
    for i in stack:
        result[i] = -1

for i in result:
    print(i, end=" ")
