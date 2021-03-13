# Leetcode 645. Set Mismatch


class Solution:
    def findErrorNumbers(self, nums):
        #len_nums = len(set(nums))
        leno = [x for x in range(1, len(nums) + 1)]
        lenno = set(leno)
        result = list(set(nums) ^ lenno)
        #lennno = set([x for x in nums if nums.count(x) > 1]).pop()
        for x in nums:
            if nums.count(x) > 1:
                result.insert(0, x)
                return result






        # x = set(nums)
        # memo = {}
        # result = []
        # for i in nums:
        #     if i in memo:
        #         result.append(i)
        #     else:
        #         memo[i] += 1



        
        



            
        #print(result, y)
Run = Solution()
Run.findErrorNumbers([1,2,2,4])