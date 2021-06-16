# Leetcode 473. Matchsticks to Square

# This problem boils down to splitting an array of integers into 44 subsets where all of these subsets are:
# 1. mutually exclusive i.e. no specific element of the array is shared by any two of these subsets, and
# 2. have the same sum which is equal to the side of our square.

# Approach 1. DFS Backtracking
# T: O(4^n) - because we have a total of N sticks and for each one of those matchsticks
# we have 4 different possibilities for the subsets they might belong to
# S: O(n) - For recursive solutions, the space complexity is the stack space occupied by all the recursive
# calls. The deepest recursive call here would be of size N

# Sort the input in reverse as it's quicker to find if the input will return False
# as if the first item doesn't fit to a side, then it'll return False

class Solution:
    def makesquare(self, matchsticks):
        if not matchsticks:
            return False
        
        N = len(matchsticks)
        numSum = sum(matchsticks)
        side = numSum // 4
        if side * 4 != numSum:
            return False
        matchsticks.sort(reverse = True)
        sums = [0 for _ in range(4)]

        def dfs(ind):
            if ind == N:
                return sums[0] == sums[1] == sums[2] == side
            for i in range(4):
                if sums[i] + matchsticks[ind] <= side:
                    sums[i] += matchsticks[ind]
                    if dfs(ind + 1):
                        return True
                    sums[i] -= matchsticks[ind]
            return False
        
        return dfs(0)
Run = Solution()
Run.makesquare([1,1,2,2,2])

        # self.results = []
        # def dfs(nums, ind, target):
        #     if ind == len(nums): return True
        #     for i in range(4):
        #         if target[i] >= nums[ind]:
        #             target[i] -= nums[ind]
        #             if dfs(nums, ind + 1, target): return True
        #             target[i] += nums[ind]
        #     return False

        # if len(matchsticks) < 4: return False
        # numSum = sum(matchsticks)
        # matchsticks.sort(reverse=True)
        # if numSum % 4 != 0: return False
        # target = [numSum/4] * 4
        # aa = dfs(matchsticks,0,target)
        # print(aa)