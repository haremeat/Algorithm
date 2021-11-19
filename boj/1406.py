# 에디터
# 시작할 때 커서는 문장의 맨 뒤에 위치해있으므로 left에 모든 값을 몰아준다.
# L - 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시)
# D - 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤일 경우 무시)
# B - 커서 왼쪽의 문자를 삭제함
# P $ - $라는 문자를 커서 왼쪽에 추가함
# input = sys.stdin.readline()
# [input() for _ in range(m)]

import sys

basic = sys.stdin.readline().rstrip()
m = int(sys.stdin.readline())
# command = [input() for _ in range(m)]
left = list(basic)
right = []

# basic = "abcd"
# m = 3
# command = ["P x", "L", "P y"]

# basic = "abc"
# m = 9
# command = ["L", "L", "L", "L", "L", "P x", "L", "B", "P y"]

# basic = "dmih"
# m = 11
# command = ["B", "B", "P x", "L", "B", "B", "B", "P y", "D", "D", "P z"]

for i in range(m):
    co = sys.stdin.readline().split()

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

arr = left + right[::-1]

print(''.join(arr))