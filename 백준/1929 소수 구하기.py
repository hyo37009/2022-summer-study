'''
1929 소수 구하기
난이도: 실3
'''
import sys

input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
a = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n+1):
    if a[i]:
        if i >= m:
            primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False
for num in primes:
    print(num)