# Leetcode 1123. Lowest Common Ancestor of Deepest Leaves
# 1. Traverse tree
# 2. Everytime we move down a level, we store it in self.depth
# 3. Check for children, if none and curr node is a leaf node
# return levels


# the condition: if left == right == self.depth:
# is triggered once we have reached leaf nodes, in both left and right.
# Once left equals a leaf node, we return levels. Left now is the int levels for this depth
# Once right equals a leaf node, we return levels. Right not is the int levels for this depth
# Now that we have values for both left and right, we check if left == right == self.depth.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root):
        
        self.depth = 0
        self.dummy = None
        self.dfs(root, 0)
        return self.dummy
    
    def dfs(self, root, levels):
        self.depth = max(levels, self.depth)
        if root is None:
            return levels
        
        left = self.dfs(root.left, levels + 1)
        right = self.dfs(root.right, levels + 1)
            
        if left == right == self.depth:
            self.dummy = root
        return max(left, right)

B8 = TreeNode(8)
B7 = TreeNode(0)
B2 = TreeNode(1, B7, B8)
B6 = TreeNode(4)
B5 = TreeNode(7)
B4 = TreeNode(2, B5, B6)
B3 = TreeNode(6)
B1 = TreeNode(5, B3, B4)
BT = TreeNode(3, B1, B2)
Run = Solution()
Run.lcaDeepestLeaves(BT)
