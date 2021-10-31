
# 육각형이니까
# 2~7 : 2개 (6개까지)
# 8~19: 3개 (12개까지)
# 20~37 : 4개 (18개까지)

n = int(input())
result = 1

while True:
    result += 1
    if n <= result * 6:
        print(result)
        break



