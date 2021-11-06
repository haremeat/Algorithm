chars = "abcdefghijklmnopqrstuvwxyz"
check_string = "wowwow"


def solution(s):
    answer = []

    for char in chars:
        count = s.count(char)
        if count > 1:
            answer.append(count)

    answer.sort()

    return answer
