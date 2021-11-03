# 일곱 난쟁이

list = [int(input()) for i in range(9)]

total = sum(list)

# 출력할 것 : 입골 난쟁이의 키 (오름차순)

fake1 = 0
fake2 = 0

for i in range(9):
    for j in range(i+1, 9):
        if total - (list[i] + list[j]) == 100:
            fake1 = list[i]
            fake2 = list[j]

list.remove(fake1)
list.remove(fake2)
list.sort()

for i in list:
    print(i)
