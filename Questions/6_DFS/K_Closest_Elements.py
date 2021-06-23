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

# Solution 4:
# Binary Search to Find Left Bound
# The biggest index left bound could be is len(arr) - k
# We have an if check because only one of ind and ind + k could be included in final answer
# If arr[ind] is closer to x than arr[ind + k], this means arr[ind + k] as well as every element
# to the right of it can never be in the answer; so move right pointer to avoid considering them
    # T: O(log (n - k) + k)
        # To find the bounds takes O(log (n - k)) from binary search
        # To build final output takes O(k)
    # S: O(1)

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

    def findClosestElements_4(self, arr, k, x):
        left, right = 0, len(arr)- k
        while left < right:
            ind = left + (right - left) // 2
            # Alternative: x > (arr[ind + k] + arr[ind])/2     # I.e. if x > than the midpoint of the current window, move the window right
            if x - arr[ind] > arr[ind + k] - x:                # if x - arr[ind] > arr[ind + k] - x, move the window right
                left = ind + 1
            else:                                              # Else, left val is equal or less than right,  change right to be right bounds because left indexes are always < right indexes
                right = ind
        return arr[left:left + k]


    
Run = Solution()
Run.findClosestElements_4([0,0,1,2,3,3,4,7,7,8], 3, 5)
([1,2,3,4,5], 4, 3)
([1,1,1,10,10,10], 1, 9)

[0,0,1,2,3,3,4,7,7,8], 3, 5

5 - 0 = 5,                 8 - 5 = 3           5 - 8 = -3
5 - 0 = 5,                 7 - 5 = 2           5 - 7 = -2
5 - 1 = 4,                 7 - 5 = 2           5 - 7 = -2
5 - 2 = 3,                 4 - 5 = 1           5 - 4 = 1
5 - 3 = 2,                 3 - 5 = 2           5 - 3 = 2

# 5 - -10 = 5
# 5 - 3 = 2
# 5 - 6 = 1
# 5 - -1 = 6
# 5 - 5 = 5 