# Leetcode ?. Check if a String Contains All Binary Codes of Size K

class Solution:
    def permute(self, nums):
        if len(nums) <= 1:
            return[nums]
        
        
        answer = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1: ]
            for y in self.permute(n):
                answer.append([num]+y)
        print(answer)
        return(answer)        

p1 = Solution()
p1.permute([1,2,3])