# Leetcode 1423. Maximum Points You Can Obtain from Cards

class Solution:
    def maxScore(self, cardPoints, k):

        N = len(cardPoints) - k
        minSubArraySum = float('inf')
        j = curr = 0

        for ind, val in enumerate(cardPoints):
            curr += val
            if ind - j + 1 > N:
                curr -= cardPoints[j]
                j += 1
            if ind - j + 1 == N:
                minSubArraySum = min(minSubArraySum, curr)
        return sum(cardPoints) - minSubArraySum

Run = Solution()
Run.maxScore([1,2,3,4,5,6,1], 3)