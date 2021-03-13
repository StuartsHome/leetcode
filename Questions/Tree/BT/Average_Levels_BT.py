# Leetcode 637. Average of Levels in Binary Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        info = []
        def dfs(node, depth = 0):
            if node:
                if len(info) <= depth:
                    info.append([])
                info[depth].append(node.val)

                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)
        return [sum(s)/len(s) for s in info]

    """
    info = []
    def dfs(node, depth = 0):
        if node:
            if len(info) <= depth:
                info.append([0, 0])
            info[depth][0] += node.val
            info[depth][1] += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root)
        return [s/float(c) for s, c in info]
    """

    

R4 = TreeNode(7)
R3 = TreeNode(15)
R2 = TreeNode(20, R3, R4)
R1 = TreeNode(9)
BT = TreeNode(3, R1, R2)

Run = Solution()
Run.averageOfLevels(BT)


