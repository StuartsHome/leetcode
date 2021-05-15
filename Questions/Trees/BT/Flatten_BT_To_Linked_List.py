# Leetcode 114. Flatten Binary Tree to Linked List
# Good video: https://www.youtube.com/watch?v=pduCoCDpZMg&ab_channel=nETSETOS
# Can remove final line: 
"""
self.flatten(root.right)
for this below, and insert after first if condition.
self.flatten(root.left)
self.flatten(root.right)
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root):
        if root is None:
            return
        
        curr = root.left
        if curr:
            while curr.right:
                curr = curr.right
            curr.right = root.right
            root.right = root.left
            root.left = None
        self.flatten(root.right) # only root.right, because above algo does the left but doesn't call the right

    # Faster solution, using previous_traversal to update on each DFS traversal
    # Using helper dfs function
    """
        self.previous_traversal = None
        
        def helper(curr):
            if curr is None:
                return
            helper( curr.right )
            helper( curr.left )
            
            curr.right = self.previous_traversal
            curr.left = None
            self.previous_traversal = curr
        helper(root)
    """


p4 = TreeNode(4)
p3 = TreeNode(3)
p5 = TreeNode(6)
p2 = TreeNode(5, None, p5)
p1 = TreeNode(2, p3, p4)
p = TreeNode(1,p1, p2)
Run = Solution()
Run.flatten(p)