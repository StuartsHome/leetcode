class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head, k):
        
        # curr, prev = head, head
        # counter = 1
        # while curr:
        #     if counter == k:
        #         prev = curr
        #     print(curr.val)
        #     curr = curr.next
        #     counter += 1
        # print(prev.val)
        curr, prev = head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        


L5 = ListNode(5)
L4 = ListNode(4, L5)
L3 = ListNode(3, L4)
L2 = ListNode(2, L3)
LL = ListNode(1, L2)
Run = Solution()
Run.swapNodes(LL,2)
        