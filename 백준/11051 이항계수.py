'''
11051 이항계수
난이도 : 실3
'''

n, k = map(int, input().split())
if n // 2 < k:
    k = n - k
bi = 1
for i in range(n, n - k, -1):
    bi *= i
for i in range(1, k + 1):
    bi //= i

print(bi % 10007)