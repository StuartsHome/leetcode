# Leetcode 22. Generate Parentheses
# T: O(2 ^ 2n), i.e.  O(4^n)
# S: O(4^n)
# Time complexity: 
# For Backtrack - recursion tree is a Binary Tree with
# each tree node representing an unifinished string, e.g. "(((".
# The two tree branches are either "(" or ")", representing the character
# to be appended to the string.
# To find all the valid strings, (in worst case) we need to traverse the whole
# tree till height 2n (answer string's length)


# Only adds "(" or ")" when we know it will be a valid
# sequence.
# We do this by keeping track of the number of opening and
# closing brackets we have placed so far.
# We can start an opening brancket if we still have one
# (of n) left to place.
# We can start a closing bracket if it would not
# exceed the number of opening brackets.

class Solution:
    def generateParenthesis(self, n):
        result = []
        def dfs(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                result.append("".join(S))
                return
            if left < n:
                S.append("(")
                dfs(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(")")
                dfs(S, left, right + 1)
                S.pop()
        dfs()
        print(result)
Run = Solution()
Run.generateParenthesis(3)

# Note:
# - Catalan numbers are used in combinatorial mathematics
# - 