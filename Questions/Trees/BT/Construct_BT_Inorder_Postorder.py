# Leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal


# In comparison to preorder&inorder:
# 1. Same Time & Space complexity of O(n)
# 2. Creation of memo is the same
# 3. If statement reverses to become left > right
# 4. Use pop to access last element in postorder (root)
# 5. Recursive calls on subtrees are reversed: right before the left
# 6. 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        def helper(left, right):
            if left > right:
                return None
            
            x = postorder.pop()
            root = TreeNode(x)  # create TreeNode to insert
            val = memo[x]       # grab the index of node popped
            root.right = helper(val + 1, right)
            root.left = helper(left, val - 1)
            return root
            
            
        memo = {}
        for key, value in enumerate(inorder):
            memo[value] = key
        return helper(0, len(postorder) - 1)

B4 = TreeNode(7)
B3 = TreeNode(15)
B2 = TreeNode(20, B3, B4)
B1 = TreeNode(9)
BT = TreeNode(3, B1, B2)
Run = Solution()
Run.buildTree([9,3,15,20,7], [9,15,7,20,3])