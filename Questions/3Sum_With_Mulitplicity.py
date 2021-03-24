#  Leetcode 923. 3Sum With Multiplicity

import collections
class Solution:
    def permute(self, arr, target):
        ans = 0
        n = len(arr)
        level2 = collections.defaultdict(int)
        for i in range(2, n):                       # Suppose that we are at index i such that i>2
            for j in range(i-1):                    # We consider all possible sums ending at i
                level2[arr[j] + arr[i-1]] += 1      # level2[x] is the number of distinct pairs that sum to x
            ans = ans + level2[target - arr[i]]
            ans = ans % (10**9 + 7)
        return ans

p1 = Solution()
p1.permute([1,1,2,2,2,2], 5)

([1,1,2,2,2,2], 5)

([1,1,2,2,3,3,4,4,5,5], 8)