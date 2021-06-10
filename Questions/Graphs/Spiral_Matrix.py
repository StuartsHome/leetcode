# Leetcode 54. Spiral Matrix
# T: O(n) - every element is visited once

# The if conditions towards the end, avoids repeating the right-to-left
# or down-to-up scan if there is onlu 1 row or column in the matrix.
# In the case of: [[1,2,3]] 

# It is only added in bottom part as first two for loops it is implicit.
# Due to the while condition.

grid = [[1,2,3],[4,5,6],[7,8,9]]
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# [[1,2,3],[4,5,6],[7,8,9]]
# [[1,2,3]] 

class Solution:
    def spiralOrder(self, matrix):
        # T: O(n), S: O(n)
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        dp = [[False] * n for _ in matrix]
        # dp = [[False] * n]*m

        result = []
        d_r = [0, 1, 0, -1]                         # directions of rows
        d_c = [1, 0, -1, 0]                         # directions of cols
        row = col = arrow = 0                       # arrow determines the rows & cols to start from each iteration
        for _ in range(m * n):                      # iterate for every node in graph
            result.append(matrix[row][col])
            dp[row][col] = True
            temp_row, temp_col = row + d_r[arrow], col + d_c[arrow]
            if temp_row in range(m) and temp_col in range(n) and not dp[temp_row][temp_col]:
                row, col = temp_row, temp_col
            else:
                arrow = (arrow + 1) % 4             # if out of range, increment starting row & col
                row, col = row + d_r[arrow], col + d_c[arrow]
        return result

        # result = []
        # if len(matrix) == 0:
        #     return result
        
        # m, n = len(matrix)-1, len(matrix[0])-1
        # start_m, start_n = 0, 0
        # while start_m <= m and start_n <= n:
        #     for i in range(start_n, n + 1):
        #         result.append(matrix[start_m][i])
        #     start_m += 1
        #     for i in range(start_m, m + 1):
        #         result.append(matrix[i][n])
        #     n -= 1
        #     if start_m <= m:
        #         for i in range(n, start_n - 1, -1):
        #             result.append(matrix[m][i])
        #         m -= 1
        #     if start_n <= n:
        #         for i in range(m, start_m - 1, -1):
        #             result.append(matrix[i][start_n])
        #         start_n += 1
                
        # print(result)

"""
        # Using Generators
        if not matrix or not matrix[0]:
            return []
        ans = []
        m, n = len(matrix), len(matrix[0])
        u, d, l, r = 0, m - 1, 0, n - 1
        while l < r and u < d:
            ans.extend([matrix[u][j] for j in range(l, r)])
            ans.extend([matrix[i][r] for i in range(u, d)])
            ans.extend([matrix[d][j] for j in range(r, l, -1)])
            ans.extend([matrix[i][l] for i in range(d, u, -1)])
            u, d, l, r = u + 1, d - 1, l + 1, r - 1
        if l == r:
            ans.extend([matrix[i][r] for i in range(u, d + 1)])
        elif u == d:
            ans.extend([matrix[u][j] for j in range(l, r + 1)])
        return ans
"""
Run = Solution()
Run.spiralOrder(grid)