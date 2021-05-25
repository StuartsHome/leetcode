# Leetcode 226. Invert Binary Tree
# T: O(h) - where h is the height of our tree

"""
We go from top to bottom of our tree and if we reached the leaf, we do not do anything.
If current subtree is not a leaf, we recursively call our function for both its children,
first inverting them.
"""
class Solution:
    def invertTree(self, root):
        if root is None:
            return
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
Run = Solution()
Run.invertTree()
[4,2,7,1,3,6,9]