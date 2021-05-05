# Leetcode 45. Jump Game II
# For every jump, you want to jump as far as possible
# Curr_max is only ever used when index is greater than curr_max
# If it is, then curr_max now becomes max_edge found

class Solution:
    def jump(self, nums):
        result = 0
        curr_max = 0
        maxEdge = 0
        for i in range(len(nums)):
            if i > curr_max:
                curr_max = maxEdge
                result += 1
            maxEdge = max(maxEdge,i+nums[i])    # maxEdge is only ever the max of index + curr value
        return result

Run = Solution()
Run.jump([2,3,1,1,4])

# self.total = 0
# def knapsack(ind, path):
#     if ind > len(nums) - 1:
#         return
#     if ind == len(nums) - 1:
#         return 
#     else:
#         skip = knapsack(ind + 1, path)
#         use = knapsack(ind + 1, path + [nums[ind]])
#         self.total = min(self.total, len(path))
#     return self.total
# knapsack(0, [])
# return self.total