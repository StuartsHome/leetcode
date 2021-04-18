# Leetcode 111. Minimum Depth of Binary Tree
# if one of the subtree is None, you should return the depth of another subtree.
# if all of the subtree is not None, you should return the minimum depth of the two subtrees

class Solution():
    def minDepth(self, root):
        if not root:
            return 0
        else:
            # if one of the subtree is None, you should return the depth of another subtree.
            # if all of the subtree is not None, you should return the minimum depth of the two subtrees
            if root.left is None:
                return self.minDepth(root.right) + 1
            elif root.right is None:
                return self.minDepth(root.left) + 1
            else:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    # Elaborate alternative:
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    # Alternative
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    # More concise
    def minDepth1(self, root):
        if not root:
            return 0
        if None in [root.left, root.right]:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

"""
This can be broken down into:
if None in [root.left, root.right]:
    return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

This:
if root.left and not root.right:
    return 1 + self.minDepth(root.left)
if root.right and not root.left:
    return 1 + self.minDepth(root.right)

"""