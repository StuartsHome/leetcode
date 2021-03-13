# Leetcode ?. Intersection of Two Linked Lists

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        
        
        a_pointer = headA
        b_pointer = headB
        
        while a_pointer != b_pointer:
            a_pointer = headB if a_pointer == None else a_pointer.next
            b_pointer = headA if b_pointer == None else b_pointer.next
        return a_pointer


    # Brute Force
    """
    while headA is not None:
        pB = headB
        while pB is not None:
            if headA == pB:
                return headA
            pB = pB.next
        headA = headA.next
    return None

    """
    
    # Hash table
    """
    nodes_in_B = set()

    while headB is not None:
        nodes_in_B.add(headB)
        headB = headB.next

    while headA is not None:
        # if we find the node pointed to by headA,
        # in our set containing nodes of B, then return the node
        if headA in nodes_in_B:
            return headA
        headA = headA.next

    return None
    """


P2 = ListNode(4)
P1 = ListNode(2)
PP = ListNode(3)

L5 = ListNode(4)
L4 = ListNode(2)
L3 = ListNode(1)
L2 = ListNode(9)
LL = ListNode(1)

LL.next = L2 
L2.next = L3
L3.next = L4
L4.next = L5
PP.next = P1
P1.next = P2

Run = Solution()
Run.getIntersectionNode(LL, PP)