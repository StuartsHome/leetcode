class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        self.memo = []
        self.helper(root)
        return self.memo == sorted(self.memo) and len(set(self.memo)) == len(self.memo)
        print(self.memo)

    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        self.memo.append(root.val)
        self.helper(root.right)
        


p3 = TreeNode(3)
p5 = TreeNode(6)
p2 = TreeNode(4, p3, p5)
p1 = TreeNode(1)
p = TreeNode(5,p1, p2)
Run = Solution()
Run.isValidBST(p)

# class Solution:
#     def minDepth(self, root):
#         if not root:
#             return 0
#         else:
#             # if one of the subtree is None, you should return the depth of another subtree.
#             # if all of the subtree is not None, you should return the minimum depth of the two subtrees
#             if root.left is None:
#                 return self.minDepth(root.right) + 1
#             elif root.right is None:
#                 return self.minDepth(root.left) + 1
#             else:
#                 return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

"""
    def flatten(self, root):
        if root is None:
            return
        
        curr  = root.left
        if curr:
            while curr.right:
                curr = curr.right
            curr.right = root.right
            root.right = root.left
            root.left = None
        self.flatten(root.right)

p4 = TreeNode(4)
p3 = TreeNode(3)
p5 = TreeNode(6)
p2 = TreeNode(5, None, p5)
p1 = TreeNode(2, p3, p4)
p = TreeNode(1,p1, p2)
Run = Solution()
Run.flatten(p)
"""