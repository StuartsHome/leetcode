# Leetcode 113. Path Sum II

# Return all root-to-leaf paths where each path's sum equals targetSum

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        self.result = []
        def dfs(curr, path, total):
            if curr is None:
                return
            if curr.left is None and curr.right is None and total == curr.val:
                self.result.append(path + [curr.val])
                return
            dfs(curr.left, path + [curr.val], total - curr.val)
            dfs(curr.right, path + [curr.val], total - curr.val)
            return

        dfs(root, [], targetSum)
        return self.result

B6 = TreeNode(1)
B5 = TreeNode(13)
B7 = TreeNode(5)
B8 = TreeNode(4, B7, B6)
B2 = TreeNode(8, B5, B8)
B4 = TreeNode(7)
B9 = TreeNode(2)
B3 = TreeNode(11, B4, B9)
B1 = TreeNode(4, B3)
BT = TreeNode(5, B1, B2)
# B1 = TreeNode(2)
# BT = TreeNode(1, B1)
Run = Solution()
# Run.pathSum(BT, 1)
Run.pathSum(BT, 22)