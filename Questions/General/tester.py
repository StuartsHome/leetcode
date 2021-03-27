# class Solution:
# 	def isAnagram(self, s, t):
# 		strs = list(s)
# 		if len(strs) <= 1:
# 			return [strs]
# 		memo = []
# 		for i, val in enumerate(strs):
# 			a = strs[:i] + strs[i+1:]

# 			for y in self.isAnagram(a, t):
# 				memo.append([val]+y)
# 				if t in memo:
# 					return True
# 		return (memo)

# 	# def ppp(memo):
# 	# 	print(memo)

# p1 = Solution()
# p1.isAnagram("car", "rac")

class Solution:
    def permute(self, nums):
        visited = set()
        res = []
        self.backtracking(res,visited,[],nums)
        aa = res
        print(aa)
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
