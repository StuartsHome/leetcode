# Leetcode 605. Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        while i < len(flowerbed):
            if (flowerbed[i] == 0 and
            (i == 0 or flowerbed[i - 1] == 0) and
            (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                flowerbed[i] = 1
                n -=1
            i += 1
        return True if n <= 0 else False
    
Run = Solution()
Run.canPlaceFlowers([1,0,0,0,1], 1)
    