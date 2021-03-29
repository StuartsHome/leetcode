# Leetcode 908. Smallest Range I

class Solution:
    def smallestRangeI(self, A, K):
        minn = min(A)
        maxxer = max(A)
        diff = maxxer - minn - K * 2
        return max(0, diff)
        
Run = Solution()
Run.smallestRangeI([7,8,8], 5)
([1], 0)
([1,3,6],3)
([0,10], 2)
([1], 5)