
## Diameter of Binary Tree
```python
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def height(p):
            # it's custom to define the height of an empty tree to be -1. This also fixes the off-by-one error I mentioned.
            if not p: return -1                    
            left, right = height(p.left), height(p.right)
            # the "2+" accounts for the edge on the left plus the edge on the right. This change is required to account for 
            # the fact that we updated the height of an empty tree to be -1. 
            self.ans = max(self.ans, 2+left+right)   
            return 1+max(left, right)
        height(root)
        return self.ans     
```
## Minimum Depth of BT
```python
class Solution():
    def minDepth(self, root):
        if not root:
            return 0
        else:
            # if one of the subtree is None, you should return the depth of another subtree.
            # if all of the subtree is not None, you should return the minimum depth of the two subtrees
            if root.left is None:
                return self.minDepth(root.right) + 1
            elif root.right is None:
                return self.minDepth(root.left) + 1
            else:
                return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```
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