'''
11478 서로 다른 부분 문자열의 개수
난이도 : 실3
'''

s = input()
ss = set()
for i in range(1, len(s) + 1):
    for j in range(len(s)):
        ss.add(s[j:j + i])

print(len(ss))