# Leetcode 343. Integer Break

class Solution:
    def integerBreak(self, n):
        aa = [i for i in range(1,n+1) if n%i==0]
        
        def multiply(nums, i):
            memo = []

            # use
            use = multiply(nums, i) 
            # not use
            skip = multiply(nums, i)
            
            total = max(sum(memo), )
            return multiply()

        multiply(aa, 0)


Run = Solution()
Run.integerBreak(10)