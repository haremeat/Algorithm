# 단지번호붙이기
import sys
from collections import deque

n = int(sys.stdin.readline())
graph = {k: [] for k in range(1, n + 1)}

