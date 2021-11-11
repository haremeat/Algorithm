# 블랙잭

# 3장을 고른다 -

n = 5
m = 21
cards = [5, 6, 7, 8, 9]

n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] > m:
                continue
            else:
                result = max(result, cards[i] + cards[j] + cards[k])



print(result)


# 다른 풀이

from itertools import combinations

card_num, target_num = map(int, input().split())
card_list = list(map(int, input().split()))
biggest_sum = 0

for cards in combinations(card_list, 3):
    temp_sum = sum(cards)
    if biggest_sum < temp_sum <= target_num:
        biggest_sum = temp_sum

print(biggest_sum)


