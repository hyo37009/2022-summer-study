n = int(input())
nums = list(range(1, n+1))

while len(nums) > 1:
    nums.pop(0)
    nums.append(nums.pop(0))

print(nums[0])