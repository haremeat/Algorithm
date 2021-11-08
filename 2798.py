# 블랙잭

# 3장을 고른다 -

n = 5
m = 21
cards = [5, 6, 7, 8, 9]

n, m = map(int, input().split())
cards = list(int(input()) for _ in range(n))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] > m:
                continue
            else:
                result = max(result, cards[i] + cards[j] + cards[k])



print(result)



