# Leetcode 1721. Swapping Nodes in a Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head, k):
        # One pass - Only swapping the vals, not the object
        curr = first = head
        second = None
        counter = 1
        while curr:
            second = None if second == None else second.next
            if counter == k:
                first = curr
                second = head
            #if second: second = second.next    
            # This line is removed because the first line in the while loop is None until the If condition is met
            curr = curr.next
            counter += 1

        temp = first.val
        first.val = second.val
        second.val = temp
        return head


        # 2. Two Passes and convert to array using additional Data Structure
        """
        if head is None:
            return None
        result = []
        while head:
            result.append(head.val)
            head = head.next
        print(result)

        if len(result) == 1:
            return head
        a = result[k-1]
        b = result[-k]
        result[k-1] = b
        result[-k] = a
        
        def lst2link(lst):
            cur = dummy = ListNode(0)
            for e in lst:
                cur.next = ListNode(e)
                cur = cur.next
            return dummy.next
        return lst2link(result)
        """
        




L4 = ListNode(50)
L3 = ListNode(40, L4)
L2 = ListNode(30, L3)
L1 = ListNode(20, L2)
LL = ListNode(10, L1)
Run = Solution()
Run.swapNodes(LL, 2)





