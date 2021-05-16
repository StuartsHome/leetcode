# Leetcode 1423. Maximum Points You Can Obtain from Cards


# Problem Translation: Find the smallest subarray sum of len(cardPoints) - k
class Solution:
    def maxScore(self, cardPoints, k):

        # Sliding Window - Simple
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

        # Sliding Window 2 - Harder
        left = 0
        right = len(cardPoints) - k
        total = sum(cardPoints[right:])
        best = total
        for _ in range(k):
            total += cardPoints[left] - cardPoints[right]
            best = max(best, total)
            left += 1
            right += 1
        return best

        # Sliding Window 3 - Harder Yet 
        s = sum(cardPoints[:k])
        res = s
        for i in range(1, k+1):
            s += cardPoints[-i] - cardPoints[k-i]
            res = max(res, s)
        return res

Run = Solution()
Run.maxScore([1,2,3,4,5,6,1], 3)