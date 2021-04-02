# Leetcode 234. Palindrome Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        # Slow
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return True if result[::-1] == result else False 

        # Fast

        if not head or not head.next:
            return True

        # 1. Get the midpoint (slow)
        slow = fast = cur = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        
        # 2. Push the second half into the stack
        stack = [slow.val]
        while slow.next:
            slow = slow.next
            stack.append(slow.val)

        # 3. Comparison
        while stack:
            if stack.pop() != cur.val:
                return False
            cur = cur.next
        
        return True

LL3 = ListNode(1)

LL2 = ListNode(2)
LL2.next = LL3

LL1 = ListNode(2)
LL1.next = LL2

LL = ListNode(1)
LL.next = LL1

Run = Solution()
Run.isPalindrome(LL)
