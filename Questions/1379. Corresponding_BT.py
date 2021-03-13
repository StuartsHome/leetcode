# Leetcode 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        def inorder(orig, cop):
            if orig:
                inorder(orig.left, cop.left)
                if orig is target:
                    self.ans = cop
                inorder(orig.right, cop.right)
                
        inorder(original,cloned)
        return self.ans

