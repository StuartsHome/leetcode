# Leetcode - 237 - Delete Node in a Linked List
# Node is just a reference.
# The premise is to change the current node's pointer to the next value.
# And to change the next values pointer to node.next.next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def deleteNode(self, node):
		node = node.next.val
		node.next = node.next.next


# Reverse Linked List
class Solution:
    def reverseList(self, head):
        curr, prev = head, None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# Create LL from array

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next