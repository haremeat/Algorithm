# 상수

a, b = map(int, input().split())

str_a = str(a)
str_b = str(b)

a_reverse = ""
b_reverse = ""

for i in str_a:
    a_reverse = i + a_reverse


for i in str_b:
    b_reverse = i + b_reverse


a_reverse_int = int(a_reverse)
b_reverse_int = int(b_reverse)

print(max(a_reverse_int, b_reverse_int))
