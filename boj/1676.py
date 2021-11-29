# 팩토리얼 0의 개수
# 5의 개수를 구하면 된다.
# 625부터는 500을 넘기니 셀 필요가 없다.

import sys

n = int(sys.stdin.readline())

cnt1 = (n // 5)
cnt2 = (n // 25)
cnt3 = (n // 125)

result = cnt1 + cnt2 + cnt3

print(result)
