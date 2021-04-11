# Linked Lists

## Iterative
### Reverse Linked List - Time Complexity O(n) - Space O(1)
```python
class Solution:
    def reverseList(self, head):
        curr, prev = head, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
```
## Recursive
### Reverse Linked List - Time Complexity O(n) - Space O(n)
The extra space comes from implicit stack space due to recursion.
The recursion could go up to `n` levels deep.
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        temp = ListNode(None)
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp
```