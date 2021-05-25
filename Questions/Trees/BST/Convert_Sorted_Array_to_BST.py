# Leetcode 108. Convert Sorted Array to Binary Search Tree
# T: O(n)
# S: O(log n) - possibly O(n)
    # as the maximum length of the stack is log N.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        
        def helper(left, right):
            if left >= right:
                return None
        
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid)
            node.right = helper(mid + 1, right)
            return node        
        return helper(0, len(nums))
            
    # Alternate
    # The lower bound is inclusive, higher bound exclusive
    def helper(self, nums, left, right):
        if left == right:
            return None
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, left, mid)