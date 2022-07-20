from string import ascii_lowercase


class Solution:
    def isPalindrome(self, inp: str) -> bool:
        alpha = list(ascii_lowercase)
        inp = list(inp.lower())
        for i in range(10):
            alpha.append(str(i))

        i = 0
        while i != len(inp):
            if inp[i] not in alpha:
                inp.pop(i)
            else:
                i += 1

        if inp[:] == inp[::-1]:
            return True
        return False

if __name__ == "__main__":
    pal = Solution()
    print(pal.isPalindrome("0P"))