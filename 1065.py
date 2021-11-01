# 한수

# 두 자리수일 경우
# 모두 한수

# 1~1000
# n = int(input())
n = 100
cnt = 0

#list()를 이용하면 등차수열을 만들수 있다.

# 한수 판별 함수
def hansu(num):
    result = 0

    for i in range(100, num + 1):
        nums = list(map(int, str(num)))
        # 한수일 경우
        if (nums[0] - nums[1]) == (nums[1] - nums[2]):
            result += 1

    return result


if n <= 100:
  print(99)
else:
    cnt = hansu(n)
    print(cnt)







