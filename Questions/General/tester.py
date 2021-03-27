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
		return (memo)

	# def ppp(memo):
	# 	print(memo)

p1 = Solution()
p1.isAnagram("car", "rac")