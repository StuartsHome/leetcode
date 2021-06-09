# Leetcode 1696. Jump Game VI

# Sliding window maximum w/ deque
# Deque will help us maintain the max of the k DPs before our curr ind
# Deque first element will hold the maxScore of the k DPs before ind i
# Each deque element will be a tuple or (total, ind)

# How to maintain deque - and keep property where first element is always the largest
# of the k DPs before curr ind:
# When we insert into the deque, if the back/right side of the deque has elements
# smaller than the one we are about to insert, then we need to keep popping it off,
# so the large value always bubble left towards the first element.

# We trim at either end with deque O(1) pops:

from collections import deque
class Solution:
    def maxResult(self, nums, k):
        # Sliding window deque
        dp = [0] * len(nums)
        dp[0] = nums[0]
        q = deque([(nums[0], 0)])           # list of 
        for i in range(1, len(nums)):
            dp[i] = nums[i] + q[0][0]       # q[0][0] is the largest k

            while q and q[-1][0] < dp[i]:   # while smallest element of q is smaller than dp[i]
                q.pop()
            q.append((dp[i],i))
            if i - k == q[0][1]:            # maintain q len of at most k, remove earliest from q if i - k.
                                            # This is ok because at end of iteration of i and removed for next iteration where it will be out of range of k (i.e. i - (k + 1))
                q.popleft()               
        return dp[-1]

        # TLE - T: O(n * k)
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     total = float("-inf")       # hold max k for curr ind
        #     for j in range(1, k + 1):
        #         if i - j >=0:           # verify k is inbound
        #             total = max(total, dp[i - j])
        #         else:                   
        #             continue
        #     dp[i] = nums[i] + total
        # print(dp)


Run = Solution()
Run.maxResult([1,-5,-20,4,-1,3,-6,-3], 2)
# Expected
[1, -4, -19, 0, -1, 3, -3, 0]

([1,-1,-2,4,-7,3], 2)
# Expected answer:
[1, 0, -1, 4, -3, 7]