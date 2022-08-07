'''
1920 수 찾기
난이도 : 실4
'''
import sys
print = sys.stdout.write

n1 = int(input())
nums1 = list(map(int, input().split()))

n2 = int(input())
nums2 = list(map(int, input().split()))

for num in nums2:
    if num in nums1:
        print('1\n')
    else:
        print('0\n')

