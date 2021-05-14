# Leetcode 560. Subarray Sum Equals K
# Solution 1. O(N)
import collections
class Solution:
    def subarraySum(self, nums, k):
        # Solution 1. Default Dict
        hash_table = collections.defaultdict(int)
        hash_table[0] = 1
        ans = running_sum = 0
        for x in nums:
            running_sum += x
            ans += hash_table[running_sum-k]
            hash_table[running_sum] += 1
        return ans

        # Solution 2. Dict
        hash_table, running_sum, res = {0: 1}, 0, 0
        for x in nums:
            running_sum += x
            res += hash_table.get(running_sum - k, 0)
            hash_table[cur] = hash_table.get(running_sum, 0) + 1
        return res

        # hash_table = collections.defaultdict(lambda:0)
        # has_table[0] = 1
        # total = 0
        # for x in nums:
        #     running_sum += x
        #     sum = running_sum - k
        #     if sum in hash_table:
        #         total += hash_table[sum]
        #     if running_sum == k:
        #         total += 1
        #     hash_table[running_sum] += 1
        # return total
Run = Solution()
Run.subarraySum([1,2,2,0,3,2,5], 5)
[0, 1, 3, 5, 5, 8, 10, 15]

        # TLE
"""
        # TLE - using accumalation table
        # Create accumulation table
        # Length + 1 for accumulation to work
        count = 0
        memo = [0] * (len(nums) + 1)
        for i in range(1, len(memo)):
            # print(memo[i-1], nums[i -1])
            memo[i] = memo[i - 1] + nums[i - 1]
        # Now, you have your accumalation table: memo
        # From index j (curr) see if memo[j] - memo[x] == k
        for j in range(len(nums)):
            for x in range(j + 1, len(nums) + 1):
                print(j, x, memo[x], memo[j])
                if memo[x] - memo[j] == k:
                    count += 1
        """

        # TLE - O(N^3)
"""        result = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                if total + nums[j] == k:
                    total += nums[j]
                    result += 1             
                else:
                    total += nums[j]
        print(result)"""
            

# Run = Solution()
# Run.subarraySum([1,2,2,0,3,2,5], 5)
# ([1,-1,0],0)
# ([1,2,3], 3)
# ([1,1,1], 2)