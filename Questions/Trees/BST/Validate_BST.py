# Leetcode 98
# T: O(n)
# S: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        self.memo = []
        self.helper(root)
        """
        for i in range(1, len(memo)):
            if memo[i-1] >= memo[i]:
                return False
        return True
        """
        return self.memo == sorted(self.memo) and len(set(self.memo)) == len(self.memo)

    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        self.memo.append(root.val)
        self.helper(root.right)