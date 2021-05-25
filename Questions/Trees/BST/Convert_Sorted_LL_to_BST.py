# Leetcode 109. Convert Sorted List to Binary Search Tree

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head):
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next

        def helper(left, right):
            if left >= right:
                return None
            mid = (left + right) // 2
            node = TreeNode(result[mid])
            node.left = helper(left, mid)
            node.right = helper(mid + 1, right)
            return node

        return helper(0, len(result))


# BT2 = TreeNode(3, None, None)
# BT4 = TreeNode(5, None, None)
# BT3 = TreeNode(4, None, None)
# BT1 = TreeNode(2, BT3, BT4)
# BT = TreeNode(1, BT1, BT2)
L4 = ListNode(9)
L3 = ListNode(5, L4)
L2 = ListNode(0, L3)
L1 = ListNode(-3, L2)
LL = ListNode(-10, L1)
Run = Solution()
Run.sortedListToBST(LL)