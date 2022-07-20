import collections
from typing import Deque

class Solution:
    def isPalindrome(self, s:str)->bool:
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop() != strs.popleft():
                return False
        return True


if __name__ == "__main__":
    pal = Solution()
    print(pal.isPalindrome("A man, a plan, a canal: Panama"))