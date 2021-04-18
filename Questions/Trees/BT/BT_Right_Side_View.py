# Leetcode 199. Binary Tree Right Side View

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        ans = []
        def inorder(r):
            if r is None:
                return
            if r.right:
                ans.append(r.val)
                inorder(r.right)
            # else:
            #     ans.append(r.val)
            #     inorder(r.left)
            else:
                inorder(r.left)
                if r.left is None:
                    ans.append(r.val)

        inorder(root)
        print(ans)
        """
        # From discussions
        if root==None:
            return []
        ans=[root.val]
        left=ans+self.rightSideView(root.left)
        right=ans+self.rightSideView(root.right)
        if len(right)>=len(left):
            return right
        aa = right+left[len(right):]
        return aa


BT = TreeNode(1)
p1 = TreeNode(2)
p2 = TreeNode(3)
p3 = TreeNode(4)
p4 = TreeNode(5)

BT.left = p1
BT.right = p2
p1.left = p3


Run = Solution()
Run.rightSideView(BT)


# BT.left = p1
# BT.right = p2
# p1.right = p4
# p2.right = p3