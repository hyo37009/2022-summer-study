from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = 1

        while right <= len(height):
            # 찾기
            isThere = False
            for i in range(left + 1, len(height)):
                if height[left] <= height[i]:
                    # 찾은 경우
                    right = i
                    dam = height[left]
                    if dam > height[right]:
                        dam = right
                    isThere = True
                    break
            for point in range(left + 1, right):
                result += dam - height[point]
            left = right
            # 못찾은 경우
            if not isThere:
                left += 1
                right = left + 1

        return result

if __name__ == '__main__':
    height = [4,2,3]
    s = Solution()
    print(s.trap(height))