from typing import List
from re import sub
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                    if word not in banned]

        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]




if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    s = Solution()
    print(s.mostCommonWord(paragraph, banned))
