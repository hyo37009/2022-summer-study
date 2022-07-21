from collections import deque

nums = deque()

num = int(input())
nums += list(range(1, num+1))

while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())

print(nums[0])