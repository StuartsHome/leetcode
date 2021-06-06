# Leetcode 563. Binary Tree Tilt
"""
Tree
                    1
            2               3
        4       5       6       7
    100   200 500 550
"""

# 100 + 0 + 0
# 200 + 0 + 0
# 4 + 100 + 200
# Return -> 304 for subtree
# We then do
# 500 + 0 + 0
# 550 + 0 + 0
# 5 + 500 + 550
# Return -> 1055 for subtree

# The return statement "return left + right + root.val" is needed because
# When we reach the end of the recursion of a leaf e.g. 100 + 0 + 0
# We need to add left, right and node values and return
#           2 
#       4       5
#    100  200 500 550
# Becomes
#           2
#       304  1055   
# And to calculate the subtree of 2, we take away 1055 from 304

# If we did "return left + right", it would become:
#           2
#       300  1050


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root):
        self.total = 0
        self.helper(root)
        return self.total
        
    def helper(self, root):
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.total += abs(right - left)
        return left + right + root.val

BT10 = TreeNode(550)
BT9 = TreeNode(500)
BT8 = TreeNode(200)
BT7 = TreeNode(100)
BT6 = TreeNode(7)
BT5 = TreeNode(6)
BT4 = TreeNode(5, BT9, BT10)
BT3 = TreeNode(4, BT7, BT8)
BT2 = TreeNode(3, BT5, BT6)
BT1 = TreeNode(2, BT3, BT4)
BT = TreeNode(1, BT1, BT2)
Run = Solution()
Run.findTilt(BT)