
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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


"""      
class Solution():
    def diameterOfBinaryTree(self, root):
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
        return self.ans      """

        
BT2 = TreeNode(3, None, None)
BT4 = TreeNode(5, None, None)
BT3 = TreeNode(4, None, None)
BT1 = TreeNode(2, BT3, BT4)
BT = TreeNode(1, BT1, BT2)

Run = Solution()
Run.minDepth(BT)
# Run.diameterOfBinaryTree(BT)





"""
class Solution():
    def longestPalindrome(self, s):
        total = 0
        def helper(l,r):
            aa = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                aa += 1
                l -= 1
                r += 1
            return aa
                
        N = len(s)
        for i in range(N):
            total += helper(i, i)
            total += helper(i, i + 1)
        return total              
Run = Solution()
Run.longestPalindrome("aaa")
("abc")"""


