# Iterative
class Solution:
	def preorder_Iterative(self, root):
		if root is None:
			return []
		curr, stack, results = root, [], []
		while curr or stack:
			if curr is None:
				curr = stack.pop()
			while curr:
				results.append(curr.val)
				if curr.right:
					stack.append(curr.right)
				curr = curr.left
		return results

p2 = TreeNode(3)
p1 = TreeNode(2, p2)
Tree = TreeNode(1,None, p1)
Run = Solution()
Run.preorder_Iterative(Tree)


###############
###############

class Solution:
	def pre(self, root):
		if root is None:
			return []
		curr, stack, result = root, [], []
		while curr or stack:
			if curr is None:
				curr = stack.pop()
			while curr:
				result.append(curr.val)
				if curr.right:
					stack.append(curr.right)
				curr = curr.left
		return result



class Solution:
	def inO(self, root):
		if root is None:
			return []
		curr, stack, result = root, [], []
		while curr or stack:
			while curr:
				stack.append(curr)
				curr = curr.left
			curr = stack.pop()
			result.append(curr.val)
			curr = curr.left



########## Test for Balance BST 
class Solution:
	def get_height(self, root):
		if root is None:
			return 0
		return 1 + max(self.height(root.left),  self.height(root.right))


	def is_balanced(self, root):
		if root is None:
			return True
		return (self.is_balanced(root.right) and self.is_balanced(root.left) 
		  and (abs(self.get_height(root.left) - self.get_height(root.right)) <= 1))


Run = Solution()
Run.balance(Tree)
