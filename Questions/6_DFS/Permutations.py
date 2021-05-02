# Leetcode 46. Permutations

class Solution:
    def permute(self, nums):
        result = []
        def dfs(ind, path):
            if not ind:
                result.append(path)
            
            for i in range(len(ind)):
                dfs(ind[:i]+ind[i+1:], path + [ind[i]])

        dfs(nums, [])
        print(result) 
        
Run = Solution()
Run.permute([1,2,3])


"""        res = []
        def dfs(counter, path):
            if len(path) == len(nums):
                res.append(path)
                return
            for x in counter:
                if counter[x]:
                    counter[x] -= 1
                    dfs(counter, path+[x])
                    counter[x] += 1
        dfs(Counter(nums), [])
        return res """