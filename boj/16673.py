# 고려대학교에는 공식 와인이 있다

c, k, p = map(int, input().split())
wine = 0

for i in range(1, c+1):
    wine += (k * i) + p*(i**2)


print(wine)