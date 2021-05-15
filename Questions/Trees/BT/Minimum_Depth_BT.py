# Leetcode 111. Minimum Depth of Binary Tree
# if one of the subtree is None, you should return the depth of another subtree.
# if all of the subtree is not None, you should return the minimum depth of the two subtrees

# The first recursive call is `return min(self.minDepth(root.left), self.minDepth(root.right)) + 1 `
# This breaks the whole tree into two: the left subtree and the right
# We want the minimum of both subtrees


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

# BFS - Simpler to understand
import collections
def minDepth(self, root):
    if root is None:
        return 0
    q = collections.deque()
    q.append((root, 1))

    while q:
        curr, depth = q.popleft()

        if curr.left is None and curr.right is None:
            return depth
        if curr.left:
            q.append((curr.left, depth + 1))
        if curr.right:
            q.append((curr.right, depth + 1))

