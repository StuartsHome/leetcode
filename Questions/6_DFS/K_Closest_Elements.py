# Leetcode 658. Find K Closest Elements

# Solution 1:
# Check every number in arr for its distance from x
    # T: O(n log(n) + k log(k))
        # First sort by "x - y" = O(n log(n))
        # Second sort of k elements = O(k log(k))
    # S: O(n) - sorted_arr is a copy of input arr

# Solution 2:
# Bisect & Sliding Window

# Solution 3:
# Binary search and Sliding Window
# Two pointers for sliding window to expand to contain k elements
    # T: O(log(n) + k)
        # Initial binary search to find where to start window takes O(log(n))
        # Sliding window starts with size 0 and expand 1 by 1 until size k
        # Thus it costs size O(k) to expand window
    # S: O(1)
        # We only use left and right variables that are O(1)
        # (Output) Return statement not counted towards space complexity

class Solution:
    def findClosestElements_1(self, arr, k, x):
        if len(arr) <= k:
            return arr
        result = []
        sorted_arr = sorted(arr, key = lambda y: abs(x - y))
        return sorted([sorted_arr[a] for a in range(k)])

    def findClosestElements_2(self, arr, k, x):
        # No Bisect
        if len(arr) == k:
            return arr
        i, j = 0, 0
        while i < len(arr) and arr[i] < x:
            i += 1
        j = i
        i -= 1
        
        while j - i - 1 < k:
            if i == -1:
                j += 1
                continue
            if j == len(arr) or abs(arr[i] - x) <= abs(arr[j] - x):
                i -= 1
            else:
                j += 1
        return arr[i+1: j]

    def findClosestElements_3(self, arr, k , x):
        # W/ binary search, no bisect
        left, right = 0, len(arr) - 1
        while left < right:
            ind = left + (right - left) // 2
            val = arr[ind]
            if val >= x:
                right = ind
            else:
                left = ind + 1

        right = left
        left -= 1
        while right - left - 1 < k: # While there is at least 1 more space to fill in window
            if left == -1:          # Left can be -1 because we add left +1 in return
                right += 1          # if left == -1, only increase window to the right
                continue
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        return arr[left + 1: right]



    
Run = Solution()
Run.findClosestElements_3([0,0,1,2,3,3,4,7,7,8], 3, 5)
([1,2,3,4,5], 4, 3)
([1,1,1,10,10,10], 1, 9)


# 5 - -10 = 5
# 5 - 3 = 2
# 5 - 6 = 1
# 5 - -1 = 6
# 5 - 5 = 5 