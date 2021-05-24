# Leetcode 108. Convert Sorted Array to Binary Search Tree
# T: O(n)
# S: O(log n) - possibly O(n)

class BST:
    def __init__(self,tree):
        self.right = None
        self.left = None

def arrayToBST(seq):
    if (seq == []):
        return None
    mid = ((len(seq)) // 2)
    tree = BST(seq[mid])
    tree.left = arrayToBST(seq[0:mid])
    tree.right = arrayToBST(seq[mid+1:])

    print(tree.val)

if __name__ == "__main__":
    seq = [1,2,3,4,5,6,7,8,9]
    arrayToBST(seq)