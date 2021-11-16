# 괄호

# ( 괄호면 넣고 ) 괄호가 나오면 넣었던 (를 뺀다.
# 1. 모든 과정이 끝났는데 스택이 비어있지 않음 -> 닫는 괄호 부족
# 2. 닫는 괄호 차례인데 스택이 비어있다 -> 여는 괄호 부족
# 즉, 모든 과정이 정상적으로 끝났을 때 스택이 비어있으면 yes 출력, 아닌 경우 no 츌력



n = int(input())

for i in range(n):
    data = list(input())
    stack = []
    is_empty = False

    for j in data:
        if j == "(":
            stack.append(j)
        else:
            if not stack:
                is_empty = True
                break
            else:
                stack.pop()

    if is_empty is False and not stack:
        print("YES")
    else:
        print("NO")



