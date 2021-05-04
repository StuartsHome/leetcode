# Leetcode 21. Merge Two Sorted Lists


class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = curr = ListNode(0)
        
        while l1 and l2:
            if l2.val > l1.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2        # or statement to add final element to list
        return dummy.next           # Dummy is head, and curr is current node

Run = Solution()
Run.mergeTwoLists()