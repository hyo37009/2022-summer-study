'''
18870 좌표 압축
난이도: 실2
'''

n = int(input())
nums = list(map(int, input().split()))
numdict = {}
newnums = sorted(list(set(nums)))
for i in range(len(newnums)):
    numdict[newnums[i]] = i
for i in nums:
    print(numdict[i], end=' ')