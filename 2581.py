# 소수

start_num = int(input())
last_num = int(input())

sosu_list = []

for num in range(start_num, last_num + 1):
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % 1 == 0:
                error += 1
                break
        if error == 0:
            sosu_list.append(num)
if len(sosu_list) > 0:
    print(sum(sosu_list)) # 최댓값
    print(min(sosu_list)) # 최솟값
else:
    print(-1)