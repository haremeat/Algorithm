arr = [1, 2, 3]


def most_frequent(data):
    count_list = []

    for x in data:
        count_list.append(data.count(x))

    return data[count_list.index(max(count_list))]


def solution(arr):
    answer = []
    max_data = 0

    for i in range(1, 4):
        max_data = most_frequent(arr)

    max_data_cnt = arr.count(max_data)

    if max_data == 1:
        second =  max_data_cnt - arr.count(2)
        third = max_data_cnt - arr.count(3)

        answer = [0, second, third]
    elif max_data == 2:
        first = max_data_cnt - arr.count(1)
        third = max_data_cnt - arr.count(3)

        answer = [first, 0, third]
    elif max_data == 3:
        first = max_data_cnt - arr.count(1)
        second = max_data_cnt - arr.count(2)

        answer = [first, second, 0]

    return answer


print(solution(arr))
