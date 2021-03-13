# Leetcode 623. Add One Node to Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root, v, d):
        depth = 1
        if d == 1:
            temp3 = TreeNode(v)
            temp3.left = root
            return temp3

        def dfs(val, node, depth, d_n):
            if node == None:
                return 

            if depth == d_n -1:
                ### This:
                obj = node.left
                node.left = TreeNode(val, obj)
                obj = node.right
                node.right = TreeNode(val, None, obj)

                # Or:
                obj = node.left
                obj2 = node.right
                node.left = TreeNode(val, obj, None)
                node.right = TreeNode(val, None, obj2)
            else:
                dfs(val, node.left, depth + 1, d_n)
                dfs(val, node.right, depth + 1, d_n)

         
        dfs(v, root, 1, d)
        return root

R4 = TreeNode(1)
R3 = TreeNode(3)
R1 = TreeNode(2, R3, R4)
BT = TreeNode(4, R1)

Run = Solution()
Run.addOneRow(BT, 1, 3)