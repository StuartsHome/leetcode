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

# Sqrt decompostion
# 1. Split the array into blocks w/ length of sqrt(n)
# 2. Calculate sunm of each block and store it in auxiliary memory 
# 3. To query RSQ(i, j), we will add the sums of all blocks lying inside
# and those that partially overlap with range [i... j]

from math import ceil, sqrt
class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.n = ceil(sqrt(len(nums)))
        self.bucket = [0 for _ in range(self.n)]
        for key, val in enumerate(nums):
            self.bucket[key//self.n] += val

    def update(self, index, val):
        self.bucket[index // self.n] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left, right):
        startBucket, endBucket = left//self.n, right//self.n
        if startBucket == endBucket: # only one bucket
            ans = sum(self.nums[k] for k in range(left, right + 1))
        else:
            ans = sum(self.bucket[k] for k in range(startBucket + 1, endBucket))
            ans += sum(self.nums[k] for k in range(left, (startBucket+1) * self.n)) # partial bucket (leading)
            ans += sum(self.nums[k] for k in range(endBucket * self.n, right+1))    # partial bucket (trailing)
        return ans

obj = NumArray([1,3,5])
obj.sumRange(0, 2)
obj.update(1, 2)

