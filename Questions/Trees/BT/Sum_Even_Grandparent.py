# Leetcode 1315. Sum of Nodes with Even-Valued Grandparent

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root):
        self.result = 0
        
        def helper(node, parent, grandparent):
            if node is None:
                return
            if parent and grandparent and grandparent.val % 2 == 0:
                self.result += node.val
            helper(node.left, node, parent)
            helper(node.right, node, parent)
            
        helper(root, None, None)
        return self.result

B5 = TreeNode(93)
B10 = TreeNode(1, None, B5)
B7 = TreeNode(91)
B8 = TreeNode(2, B7, B10)
B6 = TreeNode(81)
B4 = TreeNode(12, None, B6)
B3 = TreeNode(71)
B2 = TreeNode(86, None, B8)
B1 = TreeNode(52, B3, B4)
BT = TreeNode(79, B1, B2)
Run = Solution()
Run.sumEvenGrandparent(BT)


# B10 = TreeNode(1)
# B7 = TreeNode(5)
# B8 = TreeNode(3, None, B7)
# B2 = TreeNode(8, B10, B8)
# B6 = TreeNode(4)
# B5 = TreeNode(1)
# B4 = TreeNode(7, B5, B6)
# B9 = TreeNode(9)
# B3 = TreeNode(2, B9)
# B1 = TreeNode(7, B3, B4)
# BT = TreeNode(6, B1, B2)