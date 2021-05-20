class Solution:
    def combinationSum(self, nums, target):

        result = []
        nums.sort()
        def dfs(ind, path, total):
            if total == target:
                result.append(path)
                return
            if total > target:
                return
            
            for i in range(len(nums)):
                dfs(i, path + [nums[i]], total + nums[i])
            

        dfs(0, [], 0)
        return result


    
Run = Solution()
Run.combinationSum([1,2,3],5)