# Leetcode 543. Diameter of Binary Tree
# Calculate the depth of a node in the usual way: max(depth of node.left, depth of node.right) + 1.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def diameterOfBinaryTree(self, root):
        self.counter = 0
        def dfs(root):
            if root is None:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            self.counter = max(self.counter, left_height + right_height)
            return 1 + max(left_height, right_height)
        dfs(root)
        return self.counter
            

"""class Solution:
    def diameterOfBinaryTree(self, root):
        counter = [0]
        self.helper(root, counter)
        return counter

    def helper(self, root, counter):
        if root is None:
            return 0
        left_height = self.helper(root.left, counter)
        right_height = self.helper(root.right, counter)
        counter[0] = max(counter[0], left_height + right_height)
        return 1 + max(left_height, right_height)"""

BT2 = TreeNode(3, None, None)
BT4 = TreeNode(5, None, None)
BT3 = TreeNode(4, None, None)
BT1 = TreeNode(2, BT3, BT4)
BT = TreeNode(1, BT1, BT2)

Run = Solution()
Run.diameterOfBinaryTree(BT)