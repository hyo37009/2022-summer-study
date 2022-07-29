from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            now = list(i)
            now.sort()
            now = ''.join(now)
            if now not in result.keys():
                result[now] = [i]
            else:
                result[now] += [i]
        return list(result.values())



if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    s = Solution()
    print(s.groupAnagrams(strs))