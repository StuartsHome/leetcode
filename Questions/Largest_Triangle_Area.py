# Leetcode 812. Largest Triangle Area
"""
area of triangle = 
    area = abs(Ax(By - Cy) + Bx(Cy - Ay) + Cx(Ay - By)) / 2

"""

class Solution:
    def largestTriangleArea(self, points):
        N = len(points)
        ma = 0
        def calArea(x1, y1, x2, y2, x3, y3):
            return abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
        for i in range(N-2):                # The three for loops are offset to allow the final loop to be (i - 2), (j - 1) (k)
            for j in range(i+1, N-1):       # sequential, all start 1 index after the other
                for k in range(j+1, N):
                    ma = max(ma, calArea(points[i][0],points[i][1],points[j][0],points[j][1],points[k][0],points[k][1]))
        return ma


# Using itertools combinations and argument unpacking
from itertools import combinations
class Solution:
    def largestTriangleArea(self, points):
        def area(A, B, C):
            return abs(A[0] * (B[1] - C[1]) + B[0]*(C[1] - A[1]) + C[0] * (A[1] - B[1])) / 2
        triples = combinations(points, 3)
        maxArea = 0
        for triple in triples:
            maxArea = max(maxArea, area(*triple))
        return maxArea
        """
        return max(map(lambda x : area(*x), (combinations(points, 3)) # Single line instead of for loop above
        # For each three points use lambda to apply the area function
        """


Run = Solution()
Run.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]])


