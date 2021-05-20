# Leetcode 40. Combination Sum II
# Unique combinations, each number in candidates used once
# Sort to avoid duplicates

# Time: O(2^n)
    # Worst case - exhaust all possible combinations from input
        # Assume each number is unique
        # The number of combination for an array of size N woulf be 2^n
        # i.e. each number is either included or excluded in combination
    # Sorting: O(nlogn)
# Space: O(n)

"""
1. Sort the input to group the numbers together
2. Iterate through the sorted array to build combinations
3. To avoid generating duplicate combinations we:
3.1. next_curr > curr: we will pick the number at the current curr position into the combination, regardless the other conditions.
This is important, since the iteration should allow us to select multiple instances of a unique number into the combination.
3.2. candidates[next_curr] == candidates[next_curr-1]: we will skip the occurances all repetitive numbers in-between,
e.g. we skip the second and third occurance of number 2 in this round of backtracking.
4. Early stopping: once the sum is greater than target

"""



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()
        def dfs(ind, path, total):
            if total == target and path not in result:
                result.append(path)
                return
            if total > target:
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                dfs(i + 1, path + [candidates[i]], total + candidates[i])
        
        
        dfs(0, [], 0)
        return result