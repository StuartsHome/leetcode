# Leetcode 698. Partition to K Equal Sum Subsets


# Leetcode 698. Partition to K Equal Sum Subsets

# This problem requires the condition that every element is used
# Use an extra list to track used elements.


# Tips:
# 1. No total, use K to keep track of steps left
# 2. Everytime we find a combination that matches target, reduce k by 1
# and mark the indexes in visited as True to not visit them again.
# 3. Once k == 0, we
class Solution:
    def canPartitionKSubsets(self, nums, k):
        # Solution 2. No sort - requires ind parameter in helper dfs
        target = sum(nums) / k
        if sum(nums) % k != 0:
            return False
        visited = [False for i in nums]
        def helper(ind, total, k):
            if k == 1 and total == target:
                return True
            if total == target:
                return helper(0,0, k - 1)
            for i in range(ind, len(nums)):     
                if visited[i] == False:
                    if nums[i] + total <= target:
                        visited[i] = True                     # Make sure helper uses i + 1 and not ind + 1
                        if helper(i + 1, total + nums[i], k): # Use current value of k, as we haven't met target yet for this subset
                            return True
                        else:
                            visited[i] = False
            return False
        return helper(0, 0, k)


        # Solution 1. uses sort - becuase doesn't have ind parameter in helper dfs
        # target = sum(nums) / k
        # if sum(nums) % k != 0:
        #     return False
        # nums.sort(reverse = True)   # Requires reverse sort to stop TLE
        # visited = [False for i in nums]
        # def helper(total, k):
        #     if k == 0:
        #         return True
        #     if total == target:     # We have found a subset, reduce K by 1
        #         return helper(0, k-1)
        #     for i in range(len(nums)):
        #         if visited[i] == False:
        #             if nums[i] > target:
        #                 return False
        #             if total + nums[i] <= target:
        #                 visited[i] = True
        #                 if helper(total + nums[i], k):  
        #                     return True
        #                 else:
        #                     visited[i] = False
        #     return False

        # return helper(0, k)

Run = Solution()
Run.canPartitionKSubsets([1,1,1,1,2,2,2,2], 4)
([129,17,74,57,1421,99,92,285,1276,218,1588,215,369,117,153,22], 3)
([1,1,1,1,2,2,2,2], 4)
([1,2,3,4], 3)
([1,1,1,1,2,2,2,2],4)
([2,2,2,2,3,4,5],4)


([4,3,2,3,5,2,1], 4)
([1,2,3,4], 3)


# Index: 0, 4. total == target return True for indexes 0, 4
# Reduce K by 1
# Index: 1, 5. total == target return True for indexes 1, 5
# Reduce K by 1
# Index: 2, 6
# Reduce K by 1
# Index: 3, 7
# Reduce K by 1
# return from current stack and k == 0, return True



