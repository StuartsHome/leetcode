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
        # Preprocessing     - O(n)
        # Range Sum Query   - O(log n)
        # Update            - O(log n)

# Sqrt decompostion
# 1. Split the array into blocks w/ length of sqrt(n)
# 2. Calculate sunm of each block and store it in auxiliary memory 
# 3. To query RSQ(i, j), we will add the sums of all blocks lying inside
# and those that partially overlap with range [i... j]

from math import ceil, sqrt
class NumArray:
    # def __init__(self, nums):
    #     self.nums = nums
    #     self.n = ceil(sqrt(len(nums)))              # The number of buckets
    #     self.bucket = [0 for _ in range(self.n)]    # Initialise each bucket at 0
    #     for key, val in enumerate(nums):            # The sum of each bucket
    #         self.bucket[key//self.n] += val

    # def update(self, index, val):
    #     self.bucket[index // self.n] += val - self.nums[index]
    #     self.nums[index] = val

    # def sumRange(self, left, right):
    #     startBucket, endBucket = left//self.n, right//self.n        # get 
    #     ans = 0
    #     if startBucket == endBucket: # only one bucket
    #         ans = sum(self.nums[k] for k in range(left, right + 1))
    #     else:
    #         for k in range(startBucket +1, endBucket):          # The sums of each bucket in range
    #             ans += self.bucket[k]
    #         for k in range(left, (startBucket + 1) * self.n):   # partial bucket (leading)
    #             ans += self.nums[k]
    #         for k in range(endBucket * self.n, right + 1):      # partial bucket (trailing)
    #             ans += self.nums[k]
    #     return ans

    # Binary Indexed Tree
    def __init__(self, nums):
        self.dp = [0 for _ in range(len(nums) +1)]
        for key, val in enumerate(nums):
            self.increment(key, val)
    
    def increment(self, i, val):
        i += 1
        while i < len(self.dp):
            self.dp[i] += val
            i += i & -i                 # go to a larger range, which contains current range

    def prefix_sum(self, i):
        i += 1
        total = 0
        while i > 0:
            total += self.dp[i]
            i -= i & -i                 # got to a new range, which is immediately before current range
        return total
    
    def update(self, i, val):
        delta = val - self.sumRange(i, i)
        self.increment(i, delta)

    def sumRange(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i - 1)  

obj = NumArray([1,3,5, 10, 20, 32, 35, 40, 50, 65, 66, 67 ,100])
obj.sumRange(3, 12)
obj.update(1, 2)

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



"""