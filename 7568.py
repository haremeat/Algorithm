# 덩치

# 몸무게도 크고 키도 커야 랭크가 올라간다.

n = int(input())
people = []

for i in range(n):
    x, y = map(int, input().split())
    people.append((x, y))


for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank)