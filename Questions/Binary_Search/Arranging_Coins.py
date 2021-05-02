# Leetcode 441. Arranging Coins
# Solution 1. Exhaustive Iteration to obtain result
# Solution 2. Binary Search
"""
Assume that the answer is k, i.e. we've managed to complete k rows of coins.
These completed rows contain in total: 1 + 2 + ... + k = k(k+1) / 2 coins.
Reformulate the problem to find the maximum k such that k = k(k+1) / 2 <= N
"""

class Solution:
    def arrangeCoins(self, n):
        counter = 0
        total = 0
        summer = 0
        while summer < n and summer + total + 1 < n:
            counter += 1
            total = total + 1
            summer += total
            print(total, summer)
        return total

        # Binary Search
        left, right = 0, n
        while left <= right:
            k = left + (right - left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if curr > n:
                right = k - 1
            else:
                left = k + 1
        return right

Run = Solution()
Run.arrangeCoins(20)






