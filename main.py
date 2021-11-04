# 연습용 노트

# people = [int(input()) for _ in range(9)]

people = [20, 7, 23, 19, 10, 15, 25, 8, 13]

total = sum(people)
fake0 = 0
fake1 = 0

for i in range(8):
    for j in (i+1, 9):
        if total - (people[i] + people[j]) == 100:
            fake0 = people[i]
            fake1 = people[j]

people.remove(fake0)
people.remove(fake1)
people.sort()

for i in people:
    print(i)
