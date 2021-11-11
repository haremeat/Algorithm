# 수 찾기

# bisect_left(a, x) - 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a, x) - 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

# 이진탐색 소스코드
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)


# test case
# n = 5
# m = 5
# array_n = [4, 1, 5, 2, 3]
# array_m = [1, 3, 7, 9, 5]


n = int(input())
m = int(input())
array_n = list(map(int, input().split()))
array_m = list(map(int, input().split()))

array_n.sort()

def binary_search(array, target):

    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return 1

        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1

    return 0


for i in array_m:
    print(binary_search(array_n, i))