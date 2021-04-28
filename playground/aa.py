

class Solution:
    def combinationSum3(self, k, n):
        
        nums = [i for i in range(10)]
        # dp = [[0] * k + 1] * len(nums + 1)
        result = []
        N = len(nums) - 1
        def knapsack(ind, path, total):
            if ind == 0 or total == 0:
                return 0
            elif len(path) == k:
                return path
            elif nums[ind] > total:
                return knapsack(ind - 1, path, total)
            else:
                # skip = knapsack(ind - 1, path, total)
                use = knapsack(ind - 1, path + [nums[ind]], total - nums[ind])
                # curr = max(skip, use)
            result.append(path)
            return
        knapsack(N, [], n)
        return result

Run = Solution()
Run.combinationSum3(3, 7)
"""    weight.insert(0, 0)
    value.insert(0,0)
    N = len(weight) - 1
    def knapsack2(n, c):
        if n == 0 or c == 0: return 0
        elif weight[n] > c:
            return knapsack2(n-1, c)
        else:
            temp1 = knapsack2(n-1, c)
            temp2 = value[n] + knapsack2(n-1, c - weight[n])
            result = max(temp1, temp2)
        return result
    aa = knapsack2(N, capacity)"""