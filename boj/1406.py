# 에디터
# 시작할 때 커서는 문장의 맨 뒤에 위치해있으므로 left에 모든 값을 몰아준다.
# L - 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시)
# D - 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤일 경우 무시)
# B - 커서 왼쪽의 문자를 삭제함
# P $ - $라는 문자를 커서 왼쪽에 추가함


import sys
input = sys.stdin.readline()

# basic = input
# m = int(input)
# command = [input for _ in range(m)]
# left = command
# right = []


basic = "abcd"
m = 3
command = ["P x", "L", "P y"]

left = command
right = []


for i in command:
    co = i.split(' ')

    if co[0] == "L":
        if not left:
            pass
        else:
            left.pop()
            right.append(co[1])
    elif co[0] == "D":
        if not right:
            pass
        else:
            right.pop()
            left.append(co[1])
    elif co[0] == "B":
        left.pop()
    elif co[0] == "P":
        left.append(co[1])


result = left + right
print(result)