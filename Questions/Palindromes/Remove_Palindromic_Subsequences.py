# Leetcode 1332. Remove Palindromic Subsequences

class Solution:
    def removePalindromeSub(self, s):

        #if not s: return 0
        if s == "": return 0    # This is a faster runtime than above
        if s == s[::-1]: return 1
        return 2

Run = Solution()
Run.removePalindromeSub("abb")  