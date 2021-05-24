# Leetcode 1423. Maximum Points You Can Obtain from Cards

# T: O(n) or possibly O(k) - length of window

# Problem Translation: Find the smallest subarray sum of len(cardPoints) - k
# i.e. The smallest subarray of length len(A) - k would yield the largest sum of the other values.
class Solution:
    def maxScore(self, cardPoints, k):

        # Sliding Window - Simple
        N = len(cardPoints) - k
        minSubArraySum = float('inf')
        j = curr = 0

        for ind, val in enumerate(cardPoints):
            curr += val
            if ind - j + 1 > N:                     # Checks if the curr index is outside of window
                curr -= cardPoints[j]               # Curr is outside of window, so takeaway what just added and increase window starting index
                j += 1
            if ind - j + 1 == N:                    # The step before the curr index is outside of the window it is equal to N, save that value and replace if min
                minSubArraySum = min(minSubArraySum, curr)
        return sum(cardPoints) - minSubArraySum

        # # Sliding Window 2 - Harder
        # left = 0
        # right = len(cardPoints) - k
        # total = sum(cardPoints[right:])
        # best = total
        # for _ in range(k):
        #     total += cardPoints[left] - cardPoints[right]
        #     best = max(best, total)
        #     left += 1
        #     right += 1
        # return best

        # # Sliding Window 3 - Harder Yet 
        # s = sum(cardPoints[:k])
        # res = s
        # for i in range(1, k+1):
        #     s += cardPoints[-i] - cardPoints[k-i]
        #     res = max(res, s)
        # return res

Run = Solution()
Run.maxScore([1,2,3,4,5,6,1], 3)


"""
DFS
def maxScore(self, cardPoints, k):
    if k == len(cardPoints):
        return sum(cardPoints)
    
    def dfs(i, j, k , res = 0):
        if k == 0:
            return 0
        res = max(cardPoints[i] + dfs(i + 1, j, k - 1), cardPoints[j] + dfs(i, j - 1, k - 1))
        return res
    return dfs(0, len(cardPoints) - 1, k)
"""