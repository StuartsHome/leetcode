# Leetcode - 237 - Delete Node in a Linked List
# Node is just a reference.
# The premise is to change the current node's pointer to the next value.
# And to change the next values pointer to node.next.next

class Solution:
	def deleteNode(self, node):
		node = node.next.val
		node.next = node.next.next