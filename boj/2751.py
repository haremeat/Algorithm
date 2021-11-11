# 수 정렬하기 2

n = int(input())
m = [int(input()) for _ in range(n)]

arr = list(m)
arr.sort()

for i in arr:
    print(i)