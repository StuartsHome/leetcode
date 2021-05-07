# Leetcode ?. Delete Operations for Two Strings

class Solution:
    def minDistance(self, word1, word2):

        j = 0
        for i in word1:
            if i == word2[j]:
                j += 1
        return j
        
        



Run = Solution()
Run.minDistance("sea", "eat")
("leetcode", "etco")
