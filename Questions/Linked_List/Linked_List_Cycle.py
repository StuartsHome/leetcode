# Leetcode ?. Linked List Cycle



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):


        curr, temp = head, head.next
        while curr.next.next or curr.next:
            if curr == temp:
                return True
            curr = curr.next
            temp = curr.next.next

        print("FALSE")
        


LL3 = ListNode(-4)

LL2 = ListNode(0)
LL2.next = LL3

LL1 = ListNode(2)
LL1.next = LL2

LL = ListNode(3)
LL.next = LL1
Run = Solution()
Run.hasCycle(LL)