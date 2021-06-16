# Leetcode 437. Path Sum III
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        self.result = []
        def dfs(curr, path, total):
            if curr is None:
                return 
            if path and (total + curr.val) > targetSum:
                aa = path.pop(0)
                total -= aa
                path + [curr.val]
                total + curr.val
            if total + curr.val == targetSum:
                self.result.append(path + [curr.val])
                return
            if curr.val == targetSum:
                self.result.append([curr.val])
                return
            dfs(curr.left, path + [curr.val], total + curr.val)
            dfs(curr.right, path + [curr.val], total + curr.val)
            return
        dfs(root, [], 0)
        print(self.result)

# B8 = TreeNode(11)
# B2 = TreeNode(-3, None, B8)
# B7 = TreeNode(1)
# B4 = TreeNode(2, None, B7)
# B6 = TreeNode(-2)
# B5 = TreeNode(3)
# B3 = TreeNode(3, B5, B6)
# B1 = TreeNode(5, B3, B4)
# BT = TreeNode(10, B1, B2)
# Run = Solution()
# Run.pathSum(BT, 8)
B2 = TreeNode(-3)
# B1 = TreeNode(5, B3, B4)
BT = TreeNode(-2, None, B2)
Run = Solution()
Run.pathSum(BT, -3)