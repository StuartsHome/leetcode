# Leetcode 1690. Stone Game VII

# T: O(n^2) 
# S: O(n)

# 1. Calculate the presum
# 2. Make 2D array, N * N
# 3. DP Max of row below (i + 1) or col to left (j - 1)
# 4. Return the DP first row, last column 
 # To optomise:

"""
Use a presum array to calculate the sum of the stones
remaining in O(1) time.

This can be done because presum[i] tells us
the sum of all the stones to the left of i (inclusive).

And presum[j] tells us the sum of all the stones to
the left of j (inclusive).

So presum[j] - presum[i-1] equals sum(stones[i:j+1]) which is
the amount of points from the remaining stones in the range [i,j].
"""

class Solution:
    def stoneGameVII(self, stones):
        presum = [0] + stones[:]
        for i in range(1, len(presum)):
            presum[i] += presum[i-1]
        N = len(stones)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                aa = presum[j + 1] - presum[i + 1]          # Calculate the points of stones in ranges aa, bb
                bb = presum[j] - presum[i]
                dp[i][j] = max(aa - dp[i + 1][j], bb - dp[i][j - 1])
        for i in dp:
            print(i)
        return dp[0][N - 1]


Run = Solution()
Run.stoneGameVII([5,3,1,4,2])