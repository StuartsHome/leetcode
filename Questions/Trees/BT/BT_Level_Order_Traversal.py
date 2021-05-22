# Leetcode 102. Binary Tree Level Order Traversal

# Use a variable to track level in the tree and use simple Pre-Order Traversal
# Add sub-lists to memo as we move down the levels

# T: O(n)
# S: O(n) + O(h) for stack space
# S = O(h) because -> in worst case, stack space would be O(n), but in the best case it would be equal to the height
# of the balanced BT with n nodes, which is O(log n). It's easier to say "O(h) space where h is the height of the tree"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        self.memo = []
        self.helper(root, 0)
        return self.memo
    
    def helper(self, root, level):
        if root is None:
            return
        if len(self.memo) <= level:
            self.memo.append([])
        self.memo[level].append(root.val)
        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)

p3 = TreeNode(15)
p5 = TreeNode(7)
p2 = TreeNode(20, p3, p5)
p1 = TreeNode(9)
p = TreeNode(3,p1, p2)
Run = Solution()
Run.levelOrder(p)


# DFS + stack
"""
def levelOrder(self, root):
    if not root:
        return []
    res, stack = [], [(root, 0)]
    while stack:
        curr, level = stack.pop()
        if len(res) < level + 1:
            res.append([])
        res[level].append(curr.val)
        if curr.right:
            stack.append((curr.right, level+1))
        if curr.left:
            stack.append((curr.left, level+1))
    return res
"""