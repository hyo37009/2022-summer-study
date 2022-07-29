class Solution:
    def longestPalindrome(self, s: str) -> str:
        chars = list(s)
        result = []
        now = 1
        for i in range(1, len(s)):
            # 홀수 개 팰런드롬 조사
            if chars[now - i] == chars[now + i]:
                longest = i
                odd = True
            if chars[now - i] == chars[now + i - 1]:
                longest = i


if __name__ == '__main__':
    strr = "babad"
    s = Solution()
    s.longestPalindrome(strr)