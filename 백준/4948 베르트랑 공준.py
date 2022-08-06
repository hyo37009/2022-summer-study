'''
4948 베르트랑 공준
난이도 : 실3
'''

import sys

input = sys.stdin.readline

n = 1
while n != 0:
    n = int(input().rstrip())
    if n == 0:
        break
    nums = []
    a = [False, False] + [True] * (2 * n - 1)
    for i in range(2, 2 * n + 1):
        if a[i]:
            if n < i <= 2 * n:
                nums.append(i)
            for j in range(2 * i, 2 * n + 1, i):
                a[j] = False
    print(len(nums))