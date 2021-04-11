# Leetcode 78. Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Time Complexity - O(n * 2^n)
# Space Complexity - O(n * 2^n)
"""class Solution:
    def subsets(self, nums):
        output = [[]]

        for i in nums:
            output += [x  + [i] for x in output]
        return output
Run = Solution()
Run.subsets([1,2,3])"""

# Backtrack
# Same time complexity, but O(N) space.

# DFS from https://leetcode.com/problems/subsets-ii/discuss/750386/Python3-DFS-solutions-to-6-different-classic-backtracking-problems-and-more
class Solution:
    def subsets(self, nums):
        res = []
        def dfs(idx, path):
            res.append(path)
            for i in range(idx, len(nums)):
                dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return res
Run = Solution()
Run.subsets([1,2,3])