# 알파벳 찾기

# s = input()
s = "baekjoon"

# 알파벳 소문자 범위
alphabet = list(range(97, 123))

for x in alphabet:
    print(s.find(chr(x)))

