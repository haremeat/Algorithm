numbers = [1, 2, 3, 4, 6, 7, 8, 0]


def solution(numbers):
    answer = 0

    for i in range(10):
        if i not in numbers:
            answer += int(i)

    return answer



print(solution(numbers))