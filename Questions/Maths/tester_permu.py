# Delete this file when finished

class Solution:
    def permute(self, nums):
        visited = set()
        res = []
        self.backtracking(res,visited,[],nums)
        print(res)
    def backtracking(self,res,visited,subset,nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res,visited,subset+[nums[i]],nums)
                visited.remove(i)
p1 = Solution()
p1.permute([2,4,5,10])

([1,2,3])