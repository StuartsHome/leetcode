class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        self.result = None

        def dfs(curr):
            if curr is None:
                return False
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            mid = (curr.val == p) or (curr.val == q)

            if mid + left + right >= 2:
                self.result = curr
            return mid or left or right
        dfs(root)
        print(self.result.val)

B8 = TreeNode(8)
B7 = TreeNode(0)
B2 = TreeNode(1, B7, B8)
B6 = TreeNode(4)
B5 = TreeNode(7)
B4 = TreeNode(2, B5, B6)
B3 = TreeNode(6)
B1 = TreeNode(5, B3, B4)
BT = TreeNode(3, B1, B2)
P = TreeNode(5)
Q = TreeNode(1)
Run = Solution()
Run.lowestCommonAncestor(BT, 6, 4)