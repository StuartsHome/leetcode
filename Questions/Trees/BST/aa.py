
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
("abc")



"""class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def diameterOfBinaryTree(self, root):
        # print recursive inorder 
        if root.left != None:
            self.diameterOfBinaryTree(root.left)
        print(root.val)
        if root.right != None:
            self.diameterOfBinaryTree(root.right)

        
BT2 = TreeNode(3, None, None)
BT4 = TreeNode(5, None, None)
BT3 = TreeNode(4, None, None)
BT1 = TreeNode(2, BT3, BT4)
BT = TreeNode(1, BT1, BT2)

Run = Solution()
Run.diameterOfBinaryTree(BT)"""