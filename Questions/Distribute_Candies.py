# Leetcode 575. Distribute Candies


class Solution:
    def distributeCandies(self, candyType):
        total = len(candyType) // 2

        memo = {}
        for i in candyType:
            if i in memo:
                memo[i] += 1
            else:
                memo[i] = 1

        unique_candies = len(memo.keys())
                
        if unique_candies > total:
            return total
        return unique_candies
        

        """
        # Count the number of unique candies by creating a set with
        # candyType, and then taking its length.
        unique_candies = len(set(candyType))
        # And find the answer in the same way as before.
        return min(unique_candies, len(candyType) // 2)
        """
        


Run = Solution()
Run.distributeCandies([1,1,2,2,3,3])