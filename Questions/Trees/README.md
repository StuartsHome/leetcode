

## Sum of Binary Tree
```python
def treeSum(root):
    if root is None:
        return 0
    else:
        leftSum = treeSum(root.left)
        rightSum = treeSum(root.right)
        return root.val + leftSum + rightSum
```

## Max of Binary Tree
```python
def treeMax(root):
    if root is None:
        return float("-inf")
    else:
        leftMax = treeMax(root.left)
        rightMax = treeMax(root.right)
        return max(root.val, leftMax, rightMax)
```
## Tree Height
```python
def treeHeight(root):
    if root is None:
        return 0
    else:
        leftMax = treeHeight(root.left)
        rightMax = treeHeight(root.right)
        return 1 + max(leftMax, rightMax)
```

## Exists in Tree
```python
def existsInTree(root, value):
    if root is None:
        return False
    else:
        inLeft = existsInTree(root.left, value)
        inRight = existsInTree(root.right, value)
        return root.val == value or inLeft or inRight
```
# Reverse Tree
```python
def reverseTree(root):
    if root is None:
        return
    else:
        reverseTree(root.left)
        reverseTree(root.right)
        root.left, root.right = root.right, root.left
```


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
            if not p: return -1                    
            left, right = height(p.left), height(p.right) # Find height of left and right subtrees
            self.ans = max(self.ans, 2+left+right)      # Update diameter, plus 2 because current root has 2 edges below
            return 1+max(left, right)                   # Running DFS, so return the height of the current root
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
		return 1 + max(self.height(root.left), self.height(root.right))


	def is_balanced(self, root):
		if root is None:
			return True
		return (self.is_balanced(root.right) and self.is_balanced(root.left) 
		  and (abs(self.get_height(root.left) - self.get_height(root.right)) <= 1))
Run = Solution()
Run.balance(Tree)
```

###