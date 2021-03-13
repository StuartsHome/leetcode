# Leetcode 118. Pascal's Triangle

class Solution:
    def generate(self, numRows):
        # Solution from discussions

        triangle = []

        for row_num in range(numRows):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1
            
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num - 1][j-1] + triangle[row_num - 1][j]
            triangle.append(row)
        print(triangle)


        
Run = Solution()
Run.generate(5)