# 셀프 넘버

original_list = set()
constructor_list = set()

for i in range(1, 10001):
    original_list.add(i)
    for j in str(i):
        i += int(j)
    constructor_list.add(i)

self_num = sorted(original_list - constructor_list)

for i in self_num:
    print(i)



default = set()
remove = set()

for i in range(1, 10001):
    default.add(i)
    for j in str(i):
        i += int(j)
    remove.add(i)

self_num = sorted(default - remove)

for i in self_num:
    print(i)



