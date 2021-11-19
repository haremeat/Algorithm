# 에디터
# 시작할 때 커서는 문장의 맨 뒤에 위치해있으므로 left에 모든 값을 몰아준다.
# L - 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시)
# D - 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤일 경우 무시)
# B - 커서 왼쪽의 문자를 삭제함
# P $ - $라는 문자를 커서 왼쪽에 추가함


# import sys
# input = sys.stdin.readline()

# basic = input
# m = int(input)
# command = [input for _ in range(m)]
# left = []
# right = []


basic = "abc"
m = 9
command = ["L", "L", "L", "L", "L", "P x", "L", "B", "P y"]
left = []
right = []

for i in basic:
    left.append(i)

for i in command:
    co = i.split()

    if co[0] == "L":
        if not left:
            pass
        else:
            right.append(left[-1])
            left.pop()
    elif co[0] == "D":
        if not right:
            pass
        else:
            left.append(right[-1])
            right.pop()
    elif co[0] == "B":
        if not left:
            pass
        else:
            left.pop()
    elif co[0] == "P":
        left.append(co[1])


arr = left + right
result = ""
for i in arr:
    result += i

print(result)