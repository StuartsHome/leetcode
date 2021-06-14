# Leetcode 1690. Stone Game VII

# T: O(n^2) 
# S: O(n^2)

# Idea:
# DP table could either be: Alice's score, Bob's score, or difference of their scores
# Difference of their scores is the best solution
# Each entry in dp, i.e. dp[i][j] signifies the difference between the
# ith stone and the jth stone.
# Problem is to find the difference of scores between 0th stone and nth stone.
#



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
        accum = [0] + stones[:]
        for i in range(1, len(accum)):
            accum[i] += accum[i-1]

        N = len(stones)
        dp = [[0 for _ in stones] for _ in stones]
        
        for row in range(N -1, -1, -1):
            for col in range(row + 1, N):
                aa = accum[col + 1] -  accum[row + 1]
                bb = accum[col] - accum[row]
                dp[row][col] = max(aa - dp[row + 1][col], bb - dp[row][col - 1])
        return dp[0][N - 1]

        # The same, but worse variable names
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

# Presum
# [0, 5, 8, 9, 13, 15]

# DP
# [0, 5, 3, 7, 6]   # j = 4
# [0, 0, 3, 1, 7]   # j = 3
# [0, 0, 0, 4, 2]   # j = 2
# [0, 0, 0, 0, 4]   # j = 1
# [0, 0, 0, 0, 0]   # j = None

# N = 5
# Turn 1: i = 4, j = None
# Turn 2: i = 3, j = 4, aa = 2, bb = 4, dp[i][j] = 4 (4 - 0)
# Turn 3: i = 2, j = 3, aa = 4, bb = 1, dp[i][j] = 4 (4 - 0)
# Turn 4: i = 2, j = 4, aa = 6, bb = 5, dp[i][j] = 2 (6 - 2)
# Turn 5: i = 1, j = 2, aa = 1, bb = 3, dp[i][j] = 3 (3 - 0)
# Turn 6: i = 1, j = 3, aa = 5, bb = 4, dp[i][j] = 1 (5 - 4)
# Turn 7: i = 1, j = 3, aa = 5, bb = 4, dp[i][j] = 1 (5 - 4)
# Turn 8: i = 1, j = 4, aa = 7, bb = 8, dp[i][j] = 7 (8 - 1)
# Turn 9: i = 0, j = 1, aa = 3, bb = 5, dp[i][j] = 5 (5 - 0)