
# Leetcode 240. Search a 2D Matrix II

class Solution:
    def searchMatrix(self, matrix, target):
        # Slow solution
        for i in matrix:
            for j in i:
                if j == target:
                    return True
        return False
        
        # Faster solution
        for row in matrix:
            if row[0] <= target <= row[-1]:
                    if target in row:
                        return True
        return False



matrix = [[1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]]

Run = Solution()
Run.searchMatrix(matrix, 20)
