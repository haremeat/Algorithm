# 한수

# 두 자리수일 경우
# 모두 한수

#list()를 이용하면 등차수열을 만들수 있다.

# 1~1000
# n = int(input())
# cnt = 0

n = 1000
# 한수 판별 함수
def hansu(num):
    result = 0

    for i in range(1, num+1):
        if i < 100:
            result += 1
        else:
            nums = list(map(int, str(i)))
            # 한수일 경우
            if nums[0] - nums[1] == nums[1] - nums[2]:
                result += 1

    return result


cnt = hansu(n)
print(cnt)




# 정답
# def hansu(num):
#     hansu_cnt = 0
#     for i in range(1, num+1):
#         num_list = list(map(int,str(i)))
#         if i < 100:
#             hansu_cnt += 1  # 100보다 작으면 모두 한수
#         elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
#             hansu_cnt += 1  # x의 각 자리가 등차수열이면 한수
#     return hansu_cnt
#
# num = 210
# print(hansu(num))








