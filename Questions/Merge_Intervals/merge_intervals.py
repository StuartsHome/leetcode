# Leetcode 56. Merge Intervals
# Whenever you have a O(n^2) brute-force solution see if you can sort the input
# and apply a linear operation for a faster runtime.
# Time Complexity - O(n log n)
# Space Complexity - 
# In the worst case, the merged list is equal to the length of the input intervals list. So the space complexity is O(n), where n is the length of the input list.

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

      
Run = Solution()
Run.merge([[1,4],[1,3],[2,6],[8,10],[15,18]])  

class Solution:
    def merge(self, intervals):
        if len(intervals) == 0: 
            return []

        intervals.sort()
        stack = [intervals[0]]
        for current in intervals[1:]:
            if current[0] <= stack[-1][1]: 
                stack[-1][1] = max(current[1], stack[-1][1])
            else: 
                stack.append(current)
        return stack

Run = Solution()
Run.merge([[1,4],[1,3],[2,6],[8,10],[15,18]])