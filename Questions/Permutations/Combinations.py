# class Solution:
#     def r(self, strs):

#         def helper(left, right):
#             if left < right:
#                 strs[left], strs[right] = strs[right], strs[left]
#                 helper(left + 1, right - 1)
#         helper(0, len(strs) - 1)

# Run = Solution()
# Run.r(["h","e","l","l","o"])
# ("hello")


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        aa = head.next.next
        head, head.next = head.next, head
            
        def helper(head):
            if not head or not head.next:return head
            head, head.next = head.next, head
            head.next.next = helper(head.next.next)
            #return helper(head.next.next)
                
        head.next.next = helper(aa)
        return head
