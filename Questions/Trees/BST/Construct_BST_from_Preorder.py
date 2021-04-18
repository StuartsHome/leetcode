# Leetcode 1008. Construct Binary Search Tree from Preorder Traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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


        # Solution 2.
        # Iteration of solution 1. using a for loop instead of a while loop also,
        # uses another function within the main function provided
        # Not sure if 1. or 2. is more efficient

        """
        def preorder_search(order_list):
            if not order_list:
                return None
            root = TreeNode(order_list[0])
            index = len(order_list) #if no right child found, all the nodes will be left child
            for i in range(len(order_list)): #find the index that divides the preorder list to left and right child
                if order_list[i] > root.val:
                    index = i
                    break
            root.left = preorder_search(order_list[1:index])
            root.right = preorder_search(order_list[index:])
            return root
        return preorder_search(preorder)
        """

        # Below Solution using left and right variables
        # instead of using the slice function

        # Solution 3.
        """
        if not preorder:
            return None
        
        return self.construct(preorder, 0, len(preorder))
    
    def construct(self, preorder, l, r):
        if l >= r:
            return None
        
        root = TreeNode(preorder[l])
        i = l+1
        
        while(i < r and preorder[i] < root.val):
            i += 1
    
        root.left = self.construct(preorder, l+1, i)
        root.right = self.construct(preorder, i, i + (r-i))
        
        return root
        """




Run = Solution()
Run.bstFromPreorder([8,5,1,7,10,12])
