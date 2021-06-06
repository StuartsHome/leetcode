# Leetcode 1026. Maximum Difference Between Node and Ancestor
# T: O(n) - we visit all nodes once
# S: O(n) - we need stacks to do the recursion
# maximum depth of the recursion is the height of the tree
# which is O(n) worst case, and O(log n) in the best case.

# Brute force would be to compare every node with its ancestors.
# Time complexity would be: T: O(n^2)

# Because the problem asks for maximum difference, we only need to 
# compare the ancestors with max and min value.
# Therefore, for a given node, we only need the maximum value and the minimum
# value from the root to this node

# When we call helper, left and right carry seperate max and mins

# Use abs because curr_max or curr_min - curr.val can return negative

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root):
        # 1.
        self.max_value = 0
        def helper(curr, curr_max, curr_min):
            if curr is None:
                return
            
            self.max_value = max(self.max_value, abs(curr_max - curr.val), abs(curr_min - curr.val))
            curr_max = max(curr_max, curr.val)
            curr_min = min(curr_min, curr.val)
            helper(curr.left, curr_max, curr_min)
            helper(curr.right, curr_max, curr_min)
                
        helper(root, root.val, root.val)
        return self.max_value
        # 2. 

        ## each left and right branch return "curr_max - curr_min"
        ## so "return max(left, right)" gets the max difference
        # self.max_value = 0            
        # def helper(curr, curr_max, curr_min):
        #     if curr is None:
        #         return curr_max - curr_min
    
        #     self.max_value = max(self.max_value, abs(curr_max - curr.val), abs(curr_min - curr.val))
        #     curr_max = max(curr_max, curr.val)
        #     curr_min = min(curr_min, curr.val)
        #     left = helper(curr.left, curr_max, curr_min)
        #     right = helper(curr.right, curr_max, curr_min)
        #     return max(left, right)
        
        # helper(root, root.val, root.val)
        # return self.max_value

B7 = TreeNode(13)
B8 = TreeNode(14, B7)
B2 = TreeNode(10, None, B8)
B6 = TreeNode(7)
B5 = TreeNode(4)
B4 = TreeNode(6, B5, B6)
B3 = TreeNode(1)
B1 = TreeNode(3, B3, B4)
BT = TreeNode(8, B1, B2)
Run = Solution()
Run.maxAncestorDiff(BT)