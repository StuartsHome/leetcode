# Leetcode 235. Lowest Common Ancestor of a Binary Search Tree

# The same solution can be used for LCA for both BT and BST, however on BST this solution is far from optimal.
# T: O(N)
# S: O(N)

# The better solution:
# 1. Traverse the tree
# 2. If both the nodes p and q are in the right subtree, then continue the search with right subtree,
# starting at step 1.
# 3. If both the nodes p and q are in the left subtree, then continue the search with left subtree,
# starting step 1.
# 4. If both step 2 and step 3 are not true, this means we have found the node which is common to node
# p's and q's subtree, and hence we return this common node as the LCA.

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.result = None
        def dfs(curr):
            if curr is None:
                return False
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            mid = (curr == p) or (curr == q)

            if mid + left + right >= 2:
                self.result = curr
            return mid or left or right
        dfs(root)
        return self.result



Run = Solution()
Run.lowestCommonAncestor()

"""
def lowestCommonAncestor(self, root, p, q): 
    if p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q)

    elif p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q)

    else:
        # p and q are contained in left and right subtrees, return this node as LCA
        return root
"""