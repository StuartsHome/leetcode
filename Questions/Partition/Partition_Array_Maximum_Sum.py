# Leetcode 1043. Partition Array for Maximum Sum
# dp[i] record the maximum sum we can get considering arr[0] - arr[i-1]
# To get dp[i], we will try to change x last numbers separately to the maximum of them,
# where x = 1 to x = k

# Time O(nk), space O(n)

class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        N = len(arr)
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            currMax = 0
            for x in range(1, min(k, i) + 1):
                currMax = max(currMax, arr[i - x])
                dp[i] = max(dp[i], dp[i - x] + currMax * x)
        return dp[N]
Run = Solution()
Run.maxSumAfterPartitioning([1,15,7,9,2,5,10],3)


"""
1,15,7,9,2,5,10
15,7,9                k = 3, i = 1
7,



For each element i, get the max 
Second for loop iterates only upto upto, k or i + 1, whichever is smaller
"""