


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root):
        self.max_value = 0
        def helper(curr, curr_max, curr_min):
            if curr is None:
                return curr_max - curr_min


            aa = abs(curr_max - curr.val)
            aa_no = curr_max - curr.val
            bb = abs(curr_min - curr.val)
            bb_no = curr_min - curr.val

            self.max_value = max(self.max_value, abs(curr_max - curr.val), abs(curr_min - curr.val))
            curr_max = max(curr_max, curr.val)
            curr_min = min(curr_min, curr.val)
            left = helper(curr.left, curr_max, curr_min)
            right = helper(curr.right, curr_max, curr_min)
            return max(left, right)
        
        helper(root, root.val, root.val)
        return self.max_value
        # self.max_value = 0
        # def helper(curr, curr_max, curr_min):
        #     if curr is None:
        #         return
            
        #     self.max_value = max(self.max_value, abs(curr_max - curr.val), abs(curr_min - curr.val))
        #     curr_max = max(curr_max, curr.val)
        #     curr_min = min(curr_min, curr.val)
        #     helper(curr.left, curr_max, curr_min)
        #     helper(curr.right, curr_max, curr_min)
                
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