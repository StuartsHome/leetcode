# Leetcode 1400. Construct K Palindrome Strings
# Condition 1. Count the occurences of all characters
# if one character has odd occurences
# there must be at least one palindrome
# with odd length and this character in the middle

# So we count the characters that appear odd times,
# the number of odd characters should not be bigger than k.

# Logic:
# k, s.size() are relatively large - 10^5, so no backtracking, brute-force is applicable.
# It's either dynamic programming or pure array logic

class Solution:
    def canConstruct(self, s, k):
        memo = {}
        for i in s:
            if i in memo:
                memo[i] += 1
            else:
                memo[i] = 1
        counter = 0
        for i in memo.values():
            if i & 1:              # Bitwise "and", returns 1 if "i" is odd, zero if even
                counter += 1
        
        return True if counter <= k <= len(s) else False


Run = Solution()
Run.canConstruct("annabelle",2)