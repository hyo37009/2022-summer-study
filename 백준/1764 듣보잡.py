'''
1764 듣보잡
난이도 : 실4
'''

n, m = map(int, input().split())
nHear = []
nSaw = []
for _ in range(n):
    nHear.append(input())
for _ in range(m):
    nSaw.append(input())

nHearAndSaw = set(nHear)&(set(nSaw))
print(len(nHearAndSaw))
print('\n'.join(sorted(nHearAndSaw)))