class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s[::-1]

        return s

if __name__ == "__main__":
    pal = Solution()
    print(pal.reverseString("A man, a plan, a canal: Panama"))