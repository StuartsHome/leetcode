
# Leetcode 389. Find the difference
# Not the optimal solution!
# Read the solution tab in leetcode - current runtime 5.5%

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        if len(s) == 0:
            print(t[0])
        
        memo = {}
        for i in s:
            if i in memo:
                memo[i] += 1
            else:
                memo[i] = 1
        
        for j in t:
            if j in memo and memo[j] > 0:
                memo[j] -= 1
            else:
                print(j)

Run = Solution()
Run.findTheDifference("a", "aa")

("abcd", "abcde")