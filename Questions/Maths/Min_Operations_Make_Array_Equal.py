# Leetcode 1551. Minimum Operations to Make Array Equal

class Solution:
    def minOperations(self, n):
        total = 0
        memo = [x * 2 + 1 for x in range(n)]
        target = sum(memo) / n
        for i in range(target, len(memo)):
            if (i - target) >= 0:
                total += i - target
        return total

Run = Solution()
Run.minOperations(6)



# 1, 3, 5, 7, 9, 11