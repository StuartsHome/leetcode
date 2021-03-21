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

####################
# Anagrams
# 1.

class Solution:
	def isAnagram(self, s, t):
		strs = list(s)
		if len(strs) <= 1:
			return [strs]
		memo = []
		for i, val in enumerate(strs):
			a = strs[:i] + strs[i+1:]

			for y in self.isAnagram(a, t):
				memo.append([val]+y)
				if t in memo:
					return True
		return self.ppp(memo)

	def ppp(memo):
		print(memo)

p1 = Solution()
p1.isAnagram("car", "rac")

########
# 2. 

from itertools import permutations

class Solution:
	def isAnagram(self, s, t):
		if len(s) != len(t):
			return False
		memo = {}
		for i in s:
			if i in memo:
				memo[i]=memo[i]+1
			else:
				memo[i]=1
		for i in t:
			if i in memo:
				if memo[i] > 0:
					memo[i] = memo[i] -1
				else:
					return False
		print(len(memo))
		print(len(memo2))
		return True
p1 = Solution()
p1.isAnagram("anagram", "nagaramp")


#########

from itertools import permutations
class Solution:
	def time(self, nums):
		max_time = 0
		for i,j,k,l in permutations(nums):
			hour = i *10 + j
			minute = k * 10 + l
			if hour < 24 and minute < 60:
				print(hour, minute)
				max_time = max(max_time, hour * 60 + minute) 
		if max_time == 0:
			return ""
		else:
			return "{:2d}:{:2d}".format(max_time // 60, max_time % 60)
p1 = Solution()
p1.time([1,2,3,4])


# Valid parentheses using hash map
# My version - different from Leetcode example
# below is generate parenthesis the most efficent method

class Solution:
	def parentheses(self, str):
		
		stack = []
		lookup = {")": "(", "}":"{", "]":"["}

		for i in str:
			if i == "(" or i == "{" or i == "[":
				stack.append(i)
			elif len(stack) < 1:
				return False
			else:
				temp = stack.pop()
				#if lookup[i] != temp:
				#	return False
		return not stack
		
p1 = Solution()
p1.parentheses("(({}))")

class Solution:
	def backTrack(self, num):
		memo = []
		for i in a:
			if len(temp) == num*2:
				valid()
			else:
				memo.append("(")
				self.backtrack(")")
				memo.pop()
				memo.append(")")
				self.backtrack(")")

		ans = []
		return ans

	def valid():
		pass

p1 = Solution()
p1.backTracks(6)

#  Construct parentheses string from an int
class Solution:
	def backTrack(self, num):
		memo = []
		def repeat(s ="", left = 0, right = 0):
			if len(s) == num*2:
				memo.append("".join(s))
			if left < num:
				 repeat(s+"(", left + 1, right)
			if right < left:
				repeat(s+")", left, right+1)
		
		repeat()
		return memo

p1 = Solution()
p1.backTrack(6)
