# Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal

# First item in preorder is root
# If we know the position of root, we can recursively split the entire array
# into two subtrees.
# Find index of root in inorder
# Create a new TreeNode of index value

# Solution 2, T: O(n^2), S: O(n^2)
# Slicing in Python creates a new list (extra space)
# For each recursive call of input N, we do O(n).
# Thus n * n = n^2
# list.index = O(n) & recursive call = O(n), we can change the "list.index" to dict for better O(1) runtime

# Hashmap solution:
# T: O(n)
# S: O(n)
# Build hashmap takes O(n), as there are n nodes to add
# Adding items to hashmap is O(1)
# Building tree is O(n). The recursive helper method has a cost of O(1) for each call
# it has no loops, and is called once for each of the N nodes, giving a total of O(n)

# Space, building the hasmap and storing the entire tree each requires O(n) memory.
# The size of the implicit system stack used by recursion calls depends on the height
# of the tree, which is O(n) in worst case and O(log N) on average.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        
        self.ind = 0
        def helper(left, right):
            if left > right:
                return None
            
            val = preorder[self.ind]
            root = TreeNode(val)
            self.ind += 1

            # Build left and right subtree
            root.left = helper(left, inorder_memo[val] - 1)
            root.right = helper(inorder_memo[val] + 1, right)
            return root
        
        # Build hashmap
        inorder_memo = {}
        for index, value in enumerate(inorder):
            inorder_memo[value] = index
        return helper(0, len(preorder) - 1)


        # T: O(n^2) 
        # if inorder:
        #     ind = inorder.index(preorder.pop(0))    # set first item of preorder as root
        #     root = TreeNode(inorder[ind])
        #     root.left = self.buildTree(preorder, inorder[0:ind])
        #     root.right = self.buildTree(preorder, inorder[ind + 1:])
        #     return root

Run = Solution()
Run.buildTree([3,9,20,15,7], [9,3,15,20,7])


