# Requires a Return statement at the end to end the loop
class Solution:
	def permute(self, nums):
		if len(nums) <= 1:
			return[nums]

		answer = []
		for i, val in enumerate(nums):
			num = nums[:i] + nums[i+1:]
			for y in self.permute(num):
				answer.append([val]+y)
		
		return answer




p1 = Solution()
p1.permute([1,2,3])


class Solution:
	def permute(self, nums):

		if len(nums) <= 1:
			return[nums]
		
		memo = []
		for i, val in enumerate(nums):
			a = nums[:i] + nums[i+1:]
			for y in self.permute(a):
				memo.append([val]+y)
		return memo

p1 = Solution()
p1.permute([1,2,3])




##### Alternative approach to Leetcode 46. Permutations
# This solution doesn't require a return at the end
class Solution:
    def permute(self, nums):
        visited = set()
        res = []
        self.backtracking(res,visited,[],nums)
        return res
    def backtracking(self,res,visited,subset,nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res,visited,subset+[nums[i]],nums)
                visited.remove(i)
p1 = Solution()
p1.permute([1,2,3])
