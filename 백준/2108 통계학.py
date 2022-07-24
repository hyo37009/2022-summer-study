'''
2108 통계학
난이도 : 실3
'''


import sys
import collections

n = int(input())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))

nums.sort()
a1 = round(sum(nums) / len(nums))
a2 = nums[len(nums) // 2]
common = collections.Counter(nums).most_common()
a3 = common[0][0]
if len(nums) > 1 and common[0][1] == common[1][1]:
    a3 = common[1][0]
a4 = nums[-1] - nums[0]

print(a1, a2, a3, a4, sep='\n')