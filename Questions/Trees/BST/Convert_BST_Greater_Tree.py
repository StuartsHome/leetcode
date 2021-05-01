# Leetcode 538. Convert BST to Greater Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root):

        def dfs(curr, total):       # Function with Two parameters
            if curr is None:
                return total
            curr.val += dfs(curr.right, total)
            return dfs(curr.left, curr.val)

        dfs(root, 0)
        return root

        """ alternate
        self.total = 0
        def dfs(curr):              # Function with One parameter
            if not curr:
                return 
            dfs(curr.right)
            self.total += curr.val
            curr.val = self.total
            dfs(curr.left)
        dfs(root)
        return root
        """

p4 = TreeNode(1)
p3 = TreeNode(2, p4)
p2 = TreeNode(4)
p1 = TreeNode(0, None, p3)
BST = TreeNode(3, p1, p2)

Run = Solution()
Run.convertBST(BST)