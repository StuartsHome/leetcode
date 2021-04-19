# Leetcode 5. Longest Palindromic Substring
# Code similar to Palindromic substrings
class Solution():
    def longestPalindrome(self, s):
        total = 0
        def helper(l,r):
            aa = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                aa += 1
                l -= 1
                r += 1
            return aa
                
        N = len(s)
        for i in range(N):
            total += helper(i, i)
            total += helper(i, i + 1)
        return total              
Run = Solution()
Run.longestPalindrome("aaa")

# Alternative
class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        print(res)

    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

Run = Solution()
Run.longestPalindrome("cbbd")

("babad")
        
        
        
   