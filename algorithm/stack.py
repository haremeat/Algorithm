# 스택 예제

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

stack.pop()  # 삭제

stack.append(1)
stack.append(4)

stack.pop()

print(stack)  # 최하단 원소부터 출력
# [5, 2, 3, 1]

print(stack[::-1])  # 최상단 원소부터 출력

# [1, 3, 2, 5]