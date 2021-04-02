# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# To Do:
# 1. Create a Snippet or template for easy creating BST/LL/etc.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val         
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root, low, high):
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
        """ MY CODE DOESNT WORK
        curr, prev, temp = root, root, None
        
        while curr or curr.next:
            if curr.val > high or curr.val < low:
                if curr.left: 
                    temp = curr.left
                    curr = prev
                    curr.left = temp
                elif curr.right:

                    temp = curr.right
                    curr = prev
                    curr.right = temp
                
                
            else:
                prev = curr
        """

p4 = TreeNode(1)
p3 = TreeNode(2, p4)
p2 = TreeNode(4)
p1 = TreeNode(0, None, p3)
BST = TreeNode(3, p1, p2)

Run = Solution()
Run.trimBST(BST, 1, 3)