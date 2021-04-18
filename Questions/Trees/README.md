### Construct Binary Search Tree from Preorder Traversal
```python
class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i<len(preorder) and preorder[i] < root.val:
            i+=1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
```
### Test for Balance BST 
```python
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
```

###