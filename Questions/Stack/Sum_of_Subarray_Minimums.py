# Leetcode 907. Sum of Subarray Minimums
# Find all subarrays and then generate all mins - T: O(n^3)
# While making subarrays, find min of each subarray - T: O (n^2)
# Good Video: https://www.youtube.com/watch?v=vjxBVzVB-mE&ab_channel=HappyCoding
# Good Article: https://leetcode.com/problems/sum-of-subarray-minimums/discuss/257811/Python-O(n)-slightly-easier-to-grasp-solution-(explained)

class Solution:
    def sumSubarrayMins(self, arr):
        # Using Monotonic Queue - elements from front to end are strictly increasing or decreasing
        # res = 0
        # stack = []
        # d = {}
        # for ele in arr:
        #     cur = 1
        #     while stack and stack[-1][0] >= ele:
        #         cur += stack.pop()[1]
        #     stack.append((ele, cur))
        #     d[len(stack) - 1] = (d[len(stack) - 2] if len(stack) - 2 in d else 0) + ele * cur
        #     res += d[len(stack) - 1]
        # return res % (10**9 + 7)
        stack = [-1]
        arr.append(0)
        result = 0
        for i, num in enumerate(arr):
            while arr[stack[-1]] > num:
                center = stack.pop()
                result += (i - center) * (center - stack[-1]) * arr[center]
            stack.append(i)
        return result % (10 **9 + 7)

Run = Solution()
Run.sumSubarrayMins([3,1,2,4])

# Trick: we add zeros to arr and stack to avoid dealing with boundaries)
"""
        A = [0]+arr
        result = [0]*len(A)
        stack = [0]
        for i in range(len(A)):
            while A[stack[-1]] > A[i]:
                stack.pop() 
            j = stack[-1]
            result[i] = result[j] + (i-j)*A[i]
            stack.append(i)
        return sum(result) % (10**9+7)
"""