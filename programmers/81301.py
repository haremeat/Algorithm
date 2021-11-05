# 숫자 문자열과 영단어

# 기준점을 뭘로 나눌 것인가?

from collections import OrderedDict

s = "one4seveneight"


def solution(s):
    answer = 0

    alphabet = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        s = s.replace(alphabet[i], str(number[i]))

    answer = int(s)
    return answer


print(solution(s))


# 테스트 케이스 3,6,7,8,9 실패


def solution(s):
    answer = ''
    words = {'zero': '0',
             'one': '1',
             'two': '2',
             'three': '3',
             'four': '4',
             'five': '5',
             'six': '6',
             'seven': '7',
             'eight': '8',
             'nine': '9'}
    word = ''
    for i in s:
        if i.isdigit():
            answer += i
            continue
        word += i
        if word in words:
            answer += words[word]
            word = ''
    return int(answer)
