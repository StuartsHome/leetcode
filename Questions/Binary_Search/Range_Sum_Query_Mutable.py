# Leetcode 307. Range Sum Query - Mutable

# Solutions:
# 1. Naive - Brute Force: TLE
    # 1. Time Complexity is:
        # Range Sum - O(n)
        # Update    - O(1)        
# 2. Sqrt Decomposition - T: O(n), S: O(sqrt(n))
    # 1. Time complexity is:
        # Preprocessing     - O(n)
        # Range Sum Query   - O(sqrt(n))
        # Update            - O(1)
    # Space Complexity:
        # We need additional sqrt(n) memory to store all block sums.
# 3. Binary Indexed Tree (Fenwick Tree)
    # Time Complexity:
        # Preprocessing     - O(n log n)  - n elements and for every element takes log n to update itself and nodes to right
        # Range Sum Query   - O(log n)  - The time taken will be the height of the Binary Indexed Tree, which at worst case will be O(log(n))
        # Update            - O(log n)
    # Space:
        # O(n)

# Sqrt decompostion
# 1. Split the array into blocks w/ length of sqrt(n)
# 2. Calculate sunm of each block and store it in auxiliary memory 
# 3. To query RSQ(i, j), we will add the sums of all blocks lying inside
# and those that partially overlap with range [i... j]

from math import ceil, sqrt
class NumArray:
    # Sqrt Decomposition
    # def __init__(self, nums):
    #     self.nums = nums
    #     self.n = ceil(sqrt(len(nums)))              # The number of buckets
    #     self.bucket = [0 for _ in range(self.n)]    # Initialise each bucket at 0
    #     for key, val in enumerate(nums):            # The sum of each bucket / Tells what bucket each value should be placed in
    #         self.bucket[key//self.n] += val

    # def update(self, index, val):                                 # 2 Steps to update
    #     self.bucket[index // self.n] += val - self.nums[index]    # 1. Find which bucket we need to update, and update the whole bucket total by the difference between new value and old value
    #     self.nums[index] = val                                    # 2. Update the old value with the new value

    # def sumRange(self, left, right):
    #     startBucket, endBucket = left//self.n, right//self.n        # Find which bucket left & right are in 
    #     ans = 0
    #     if startBucket == endBucket: # only one bucket
    #         ans = sum(self.nums[k] for k in range(left, right + 1))
    #     else:
    #         for k in range(startBucket +1, endBucket):          # Left & Right fully lie within range Start&End Bucket so add the full totals to total
    #             ans += self.bucket[k]
    #         for k in range(left, (startBucket + 1) * self.n):   # partial bucket (leading)
    #             ans += self.nums[k]
    #         for k in range(endBucket * self.n, right + 1):      # partial bucket (trailing)
    #             ans += self.nums[k]
    #     return ans

    # Binary Indexed Tree - Fenwick Tree
    def __init__(self, nums):
        self.dp = [0 for _ in range(len(nums) +1)]
        for key, val in enumerate(nums):
            self.increment(key, val)
    
    def increment(self, i, val):        # Used for filling self.dp in O(log n) and go back up the tree - O(log n)
        i += 1                          # Given index i, the next node on the access path back up to the root in which we go right
        while i < len(self.dp):         # is given by taking the binary representation of i and replacing the last 1 w/ a "0".
            self.dp[i] += val
            i += i & -i                 # does two's complement and add's to original index

    def _prefix_sum(self, i):           # Get parent - Traverse up the tree from index i
        i += 1                          # Uses bitwise "and" - the bit pattern is an intersection of the operator’s arguments.
        total = 0                       
        while i > 0:                    
            total += self.dp[i]         
            i -= i & -i                 # flips the least significant bit
        return total
    
    def update(self, i, val):               
        delta = val - self.sumRange(i, i)   # find the difference between curr val at index and val to update 
        self.increment(i, delta)            # Add that difference to every left node up the tree

    def sumRange(self, i, j):
        return self._prefix_sum(j) - self._prefix_sum(i - 1)  

obj = NumArray([1,3,5, 10, 20, 32, 35, 40, 50, 65, 66, 67 ,100])
obj.sumRange(3, 12)
obj.update(1, 2)
"""
Fenwick Tree - Updated version using my own variable names:
class NumArray:

    def __init__(self, nums):
        self.dp = [0 for _ in range(len(nums) + 1)]
        for ind, val in enumerate(nums):
            self._increment(ind, val)

    def _increment(self, ind, val):
        ind += 1
        while ind < len(self.dp):
            self.dp[ind] += val
            ind += ind & -ind
    
    def _prefixSum(self, ind):
        ind += 1
        counter = 0
        while ind > 0:
            counter += self.dp[ind]
            ind -= ind & -ind
        return counter

    def update(self, index, val):
        delta = val - self.sumRange(index, index)
        self._increment(index, delta)

    def sumRange(self, left, right):
        return self._prefixSum(right) - self._prefixSum(left - 1) 
"""
"""
Sqrt Decomposition - Updated version less generators and better variable names
class NumArray:
    from math import ceil, sqrt
    def __init__(self, nums):
        self.nums = nums
        self.N = ceil(sqrt(len(nums)))
        self.bucket = [0 for _ in range(self.N)]
        for key, val in enumerate(self.nums):
            self.bucket[key//self.N] += val

    def update(self, index, val):
        self.bucket[index//self.N] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left, right):
        startBucket, endBucket = left//self.N, right//self.N
        count = 0
        if startBucket == endBucket:
            for i in range(left, right + 1):
                count += self.nums[i]
        else:
            for i in range(startBucket + 1, endBucket):         
                count += self.bucket[i]
            for i in range(left, (startBucket + 1) * self.N):
                count += self.nums[i]
            for i in range(endBucket * self.N, right + 1):
                count += self.nums[i]
        return count
"""



""" 

# Creating the tree and it's layout:
# 1. Get the binary representation of each index
# 2. Flip the right most "1" bit
# 3. The result is the parent index
            0
    /     /     \     \
  1     2       4       8

0 is a parent of 1,2,4,8 because the binary representation of:
# 1 = 0001
# 2 = 0010
# 3 = 0011
# 4 = 0100
# 8 = 1000
# 10 = 1010

If you flip the right most 1 bit they become:
# 1 = 0000  = 0 (parent is 0)
# 2 = 0000  = 0 (parent is 0)
# 3 = 0010  = 2 (parent is 2)
# 4 = 0000  = 0 (parent is 0)
# 8 = 0000  = 0 (parent is 0)
# 10 = 1000 = 8 (parent is 8)
From the above list - all are children of 0, except 3 and 10, which are a children
of 2 and 8

# To get parent node in O(1):
    # Start with index of node to find parent
    # Increment index by 1 because self.dp is zero based
    # Get current index binary
    # Get current index 2's complement binary
    # AND the two binaries to find difference
    # Subtract the difference from the original index binary to find the next parent index
# To get parent node and add values as traverse up O(1):
    # The same as get parent node above +
    # initialise a total at the beginning
    # store self.dp[index] in total
    # every time index is updated to move to new parent, update total
# To fill out self.dp in O(n log n):
    # for loop over self.dp
    # increase i by 1 because we're zero index based
    # Add value to self.dp[i]
    # Now we need to find the next index to update by val
    # Get two's complement of current index
    # AND 2's complement index with original index to find difference
    # Add the difference to original index to find new index
"""
"""
0 = dummy node (root node), All ranges starting from 0 are new subtrees from dummy node(root)
index 1 = 0 + 2^0               = range = 0 - 0         = the sum of range 0,0 is stored at index 1 (1 value)
index 2 = 0 + 2^1               = range = 0 - 1         = the sum of range 0,1 is stored at index 2 (2 values)
index 3 = 2^1 + 2^0             = range = 2 - 2         = the sume of range 2,2 is stored at index 3 (1 value)
index 4 = 0 + 2^2               = range = 0 - 3         = etc ...
index 5 = 2^2 + 2^0             = range = 4 - 4
index 6 = 2^2 + 2^1             = range = 4 - 5 
index 7 = 2^2 + 2^1 + 2^0       = range = 6 - 6 (start from 2^2 + 2^1 = 6)
index 8 = 0 + 2^3               = range = 0 - 7
index 9 = 2^3 + 2^0             = range = 8 - 8 
index 10 = 2^3 + 2^1            = range = 8 - 9 
index 11 = 2^3 + 2^1 + 2^0      = range = 10 - 10 (start from 2^3 + 2^1 = 10) 

"""

"""
2's complement
7 = 111
2's complement of 7 = flip all bits and add 1
= 00 + 1 = 001

"""


# Original Implementation w/generators
# class NumArray:
#     def __init__(self, nums):
#         self.nums = nums
#         self.n = ceil(sqrt(len(nums)))              # The number of buckets
#         self.bucket = [0 for _ in range(self.n)]    # Initialise each bucket at 0
#         for key, val in enumerate(nums):            # The sum of each bucket
#             self.bucket[key//self.n] += val

#     def update(self, index, val):
#         self.bucket[index // self.n] += val - self.nums[index]
#         self.nums[index] = val

#     def sumRange(self, left, right):
#         startBucket, endBucket = left//self.n, right//self.n        # get 
#         if startBucket == endBucket: # only one bucket
#             ans = sum(self.nums[k] for k in range(left, right + 1))
#         else:
#             ans = sum(self.bucket[k] for k in range(startBucket + 1, endBucket))    # The sums of each bucket in range
#             ans += sum(self.nums[k] for k in range(left, (startBucket+1) * self.n)) # partial bucket (leading)
#             ans += sum(self.nums[k] for k in range(endBucket * self.n, right+1))    # partial bucket (trailing)
#         return ans


# Binary Indexed Tree 
# Link: https://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a
"""
- The representation is a BT of nodes, rather than array of buckets.
- An array of buckets will require a O(n) lookup to gather the value
because we have to recompute the total in the buckets by summing up the 
values in all smaller buckets.
- BT of nodes reduces this to (log n), by precomputing the total sum
of all elements before specific points in the sequence.
- Each node in the BT contains the cumulative sum of all the nodes
to the left of that given node.
             4
          /     \
         2       6
        / \     / \
       1   3   5   7

Now, we can augment each node by storing the cumulative sum of all the values including that node and its left subtree. 
Before:
[ +5] [ +1] [+15] [+11] [+52] [+28] [ +0]
  1     2     3     4     5     6     7

After:
                 4
               [+32]
              /     \
           2           6
         [ +6]       [+80]
         /   \       /   \
        1     3     5     7
      [ +5] [+15] [+52] [ +0]

One way that we can think about improving this operation would be to change what we store in the buckets.
Rather than storing the cumulative frequency up to the given point, you can instead think of just storing
the amount that the current frequency has increased relative to the previous bucket. 

# Implementation
# 1. Length of tree will be len(n) + 1, because "0" (the root node) is a dummy node
# 2. For every binary number, find the very last 1 in the number, then drop that bit off, along w/all the bits
# that come after it.
# 3. "0" = Left
# 4. "1" = Right
# 5. Lookup and update operations depend on the access path from the node back up to the root.
# 6. Lookup - only care about the right links we follow
#    Upate - only care about the left links we follow

# To compute the cumulative sum up to a node:
# 1. Write out node n in binary
# 2. Set the counter to 0
# 3. Repeat the following while n != 0
    # 1. Add in the value at node n
    # 2. Clear the rightmost 1 bit from n

# 1. Follow path back-up to root.
# 2. Update all nodes where we followed a left link upward:
    # 1. Write out node n in binary
    # 2. Set the counter to 0
    # 3. Repeat the following while n != 0
    # 4. Add in the value at node n
    # 5. Clear the rightmost 0 bit from n


"""