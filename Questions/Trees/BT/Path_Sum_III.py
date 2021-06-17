# Leetcode 437. Path Sum III
# T: O(n)
# S: O(n)

# At every stage we update memo with the sum of every node
# from root to curr node and its frequency.
# Once we've reached the leaf node, we subtract 1 from frequency
# I.e. once the left subtree has been traversed,
# all values of the sum keys in memo will be 0

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        self.result = 0
        self.memo = {0:1}           # Initialise w/ 0 to account for path starting from root 
        def dfs(curr, path, total):
            if curr is None:
                return 
            total += curr.val
            oldTotal = total - targetSum

            self.result += self.memo.get(oldTotal, 0)
            self.memo[total] = self.memo.get(total, 0) + 1
            dfs(curr.left, path + [curr.val], total)
            dfs(curr.right, path + [curr.val], total)
            self.memo[total] -= 1
        dfs(root, [], 0)
        print(self.result)

B8 = TreeNode(11)
B2 = TreeNode(-3, None, B8)
B7 = TreeNode(1)
B4 = TreeNode(2, None, B7)
B6 = TreeNode(-2)
B5 = TreeNode(3)
B3 = TreeNode(3, B5, B6)
B1 = TreeNode(5, B3, B4)
BT = TreeNode(10, B1, B2)
Run = Solution()
Run.pathSum(BT, 8)
# B2 = TreeNode(-3)
# B1 = TreeNode(5, B3, B4)
# BT = TreeNode(0, TreeNode(1), TreeNode(1))