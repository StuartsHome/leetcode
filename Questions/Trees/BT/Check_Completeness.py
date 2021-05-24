# Leetcode 958. Check Completeness of a Binary Tree
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root):
        self.memo = []
        self.helper(root, 0)
        N = len(self.memo)
        flag = True
        for j in self.memo:
            for i in j:
                if i == True and flag == False:
                    return False
                if i == False:
                    flag = False
        return True
    
    def helper(self, root, height):
        if root is None:
            if len(self.memo) <= height:
                self.memo.append([])
            self.memo[height].append(False)
            return
        
        if len(self.memo) <= height:
            self.memo.append([])
        self.memo[height].append(True)
        self.helper(root.left, height + 1)
        self.helper(root.right, height + 1)

        # BFS - Faster
        # Level order traversal, add children to BFS queue until we meet first empty node
        # For a complete BT, there should not be any node after we meet an empty node.
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])


R6 = TreeNode(7)
R4 = TreeNode(5)
R3 = TreeNode(4)
R2 = TreeNode(3, None, R6)
R1 = TreeNode(2, R3, R4)
BT = TreeNode(1, R1, R2)


# R6 = TreeNode(6)
# R4 = TreeNode(5)
# R3 = TreeNode(4)
# R2 = TreeNode(3, R6)
# R1 = TreeNode(2, R3, R4)
# BT = TreeNode(1, R1, R2)

Run = Solution()
Run.isCompleteTree(BT)
