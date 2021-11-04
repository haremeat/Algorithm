# 단어 공부

s = input().upper()
# s = "zZa".upper()

# 중복 제거 리스트
word_list = list(set(s))
cnt = []

for i in word_list:
    count = s.count(i)
    cnt.append(count)


idx = cnt.index(max(cnt))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[idx])