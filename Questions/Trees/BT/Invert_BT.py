# Leetcode 226. Invert Binary Tree

class Solution:
    def invertTree(self, root):
        if root is None:
            return
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
Run = Solution()
Run.invertTree()
[4,2,7,1,3,6,9]