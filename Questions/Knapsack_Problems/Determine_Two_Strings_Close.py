# Leetcode 1657. Determine if Two Strings Are Close
from collections import Counter
class Solution:
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False
        elif set(word1) != set(word2):
            return False
        
        s1, s2, d1, d2 = Counter(word1), Counter(word2), Counter(), Counter()
        for key, val in s1.items():
            d1[val] += 1
        for key, val in s2.items():
            d2[val] += 1
        return not (d2-d1)


Run = Solution()
Run.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff")
("abbzzca","babzzcz")


("abc","bca")