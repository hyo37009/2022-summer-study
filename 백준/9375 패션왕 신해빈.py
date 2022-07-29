'''
9375 패션왕 신해빈
난이도 : 실3
'''
import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    wears = defaultdict(list)
    n = int(input().rstrip())
    for i in range(n):
        now = list(map(str, input().rstrip().split()))
        wears[now[1]].append(now[0])

    nums = [len(wears[i]) + 1 for i in wears.keys()]
    result = 1
    for num in nums:
        result *= num

    print(result - 1)