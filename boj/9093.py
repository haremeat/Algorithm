# 단어 뒤집기

t = int(input())
string_list = [input() for _ in range(t)]

reverse_list = []
n_reverse = ""

# arr[::-1] # 처음부터 끝까지 -1칸 간격으로 ( == 역순으로)

for i in string_list:
    s_list = i.split()
    print(' '.join([j[::-1] for j in s_list]))

