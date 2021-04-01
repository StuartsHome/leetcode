# Leetcode 234. Palindrome Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return True if result[::-1] == result else False 
        




LL3 = ListNode(1)

LL2 = ListNode(2)
LL2.next = LL3

LL1 = ListNode(2)
LL1.next = LL2

LL = ListNode(1)
LL.next = LL1

Run = Solution()
Run.isPalindrome(LL)
