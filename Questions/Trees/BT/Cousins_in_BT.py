# Leetcode 993. Cousins in Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root, x, y):
        self.memo = []
        self.helper(root, 0, x, y, None)
        if self.memo[0][2] == self.memo[1][2] and self.memo[0][1] != self.memo[1][1]:
            return True
        return False
        print(self.memo)


    def helper(self, root, level, x, y, prev):
        if root is None:
            return
        if root.val == x or root.val == y:
            self.memo.append([root.val, prev, level])
        prev = root.val
        self.helper(root.left, level + 1, x, y, prev)
        self.helper(root.right, level + 1, x, y, prev)

p3 = TreeNode(4)
p5 = TreeNode(5)
p2 = TreeNode(3, None, p5)
p1 = TreeNode(2, None, p3)
p = TreeNode(1,p1, p2)
Run = Solution()
Run.isCousins(p ,5 ,4)