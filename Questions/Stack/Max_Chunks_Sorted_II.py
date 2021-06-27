# Leetcode 768. Max Chunks To Make Sorted II

# Monotonic Stack - Build an increasing, decreasing stack based on input
# Monotonic stack hint:  whenever we are expecting an increasing order array and we have
# to look backwards when the order is broken.

# In an increasing order array, whenever we encounter a value that is smaller it means
# the value is in an incorrect position in the sorted array.
# We need to look back for the correct position for the element.
# That position is the largest number that is smaller than the element.
# We care where to position the element because everything upto the element and the
# largest number that is smaller is in an incorrect position
# E.g. for [0, 1, 3, 4, 2] -> 2 is in wrong position, and elements 3, 4 and 2 are in incorrect
# positions (inclusive). (3, 4, 2) now make a separate chunk

# For a normal monotonic stack we would pop all elements to 1 and then add 2, but this question asks
# for the "largest value in each chunk when the chunk cannot be partitioned to smaller ones".
# This means we want, [0,1,4] instead of [0,1,2]

# Link: https://leetcode.com/problems/max-chunks-to-make-sorted-ii/discuss/595713/Monotonic-stack-solution-with-detailed-explanation

# T: O(n) - every element visited once
# S: O(n) - stack of max size n

class Solution:
    def maxChunksToSorted(self, arr):

        stack = []                          # Store a list of biggest elements of each chunk
        for num in arr:               
            largest = num                   # The bnumggest element from beginning to num
            while len(stack) > 0 and stack[-1] > num:
                largest = max(largest, stack.pop()) # Pop all elements in the incorrect position, we don't care about the min range
            stack.append(largest)           # All elements bigger than num was popped out of stack, so this is biggest element
        return len(stack)   

Run = Solution()
Run.maxChunksToSorted([2,1,3,4,4])
([4,2,2,1,1])
([2,1,0, 3,4,4])
([5,4,3,2,1])
