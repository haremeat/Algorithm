answer = 0

absolutes = [1, 2, 3]
signs = [False, False, True]


for i in signs:
    if i is False:
        absolutes[signs.index(i)] = -absolutes[signs.index(i)]

for i in absolutes:
    answer += i

print(answer)


def solution(absolutes, signs):
    answer = 0

    for i, j in zip(absolutes, signs):
        if j is True:
            answer += i
        elif i is False:
            answer -= i

    return answer

    return answer


print(solution(absolutes, signs))
