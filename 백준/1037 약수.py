'''
1037 약수
난이도: 브1
'''

n = int(input())
nums = sorted(list(map(int, input().split())))
realnum = 1

for i in range(n):
    nownum = nums[i]
    for j in range(i + 1, n):
        if nums[j] % nownum == 0:
            nums[j] //= nownum

for num in nums:
    realnum *= num
if len(set(nums)) == 1:
    realnum *= nums[0]

print(realnum)