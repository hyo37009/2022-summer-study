'''
14425 문자열 집합
난이도 : 실3
'''

n, m = map(int, input().split())
strings = set()
result = 0

for i in range(n):
    strings.add(input())

for i in range(m):
    now = input()
    if now in strings:
        result += 1

print(result)