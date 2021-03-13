# Leetcode 1431. Kids with the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        temp = [False] * len(candies)
        
        maximum = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                temp[i] = True
        print(temp)


Run = Solution()
Run.kidsWithCandies([2,3,5,1,3], 3)
        
 