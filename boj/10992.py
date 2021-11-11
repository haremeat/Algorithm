# 별 찍기 - 17

n = int(input())

for i in range(1, n+1):
    if i == 1:
        print(' '* (n-i),"*", sep='')
    elif i == 2:
        print("*")