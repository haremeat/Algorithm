# 손익분기점
# 고정비용 A
# 가변비용 B
# 생산대수 d
# 한 대 생산할 때마다 (B * d) + A의 비용이 든다.
#
# 노트북 가격 C
# 구해야 할 것 : 손익분기점
# 총 비용(A+B)

# a = int(input())
# b = int(input())
# c = int(input())

# a = 1000
# b = 70
# c = 170

a = 3
b = 2
c = 1

entity = 1

# 생산비용
production_cost = a + (b * entity)

# 판매비용
sales_cost = (c * entity)

# 손익분기점이 존재하지 않으면
if c < b:
    print(-1)
else:
    while sales_cost < production_cost:
        entity += 1
        production_cost = a + (b * entity)
        sales_cost = (c * entity)

    if sales_cost >= production_cost:
        print(entity + 1)

# print(sales_cost)
# print(production_cost)

a,b,c = map(int,input().split())

# 손익분기점이 존재하지 않으면
if c <= b:
    print(-1)
else:
    print(a // (c - b) + 1)











