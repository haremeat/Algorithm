num_cnt = int(input()) # 숫자의 개수
n = int(input()) # 숫자

nums = list(map(int, str(n)))

cnt = 0
for i in nums:
    cnt += i

print(cnt)