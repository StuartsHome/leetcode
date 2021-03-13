# Leetcode 941. Valid Mountain Array

class Solution:
    def validMountainArray(self, arr):
        # Mine
        for i in range(len(arr)):
            j = i
            while j < len(arr) - 1 and arr[j + 1] > arr[j]:
                j += 1
            if arr[j] > arr[j + 1]:
                while j < len(arr) - 1 and arr[j] > arr[j + 1]:
                    j += 1
                if j == len(arr) -1:
                    return True

            else:
                return False
        return False

        # Neat
        """
        N = len(arr)
        i = 0

        # walk up
        while i+1 < N and arr[i] < arr[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and arr[i] > arr[i+1]:
            i += 1

        return i == N-1
        """
         

Run = Solution()
Run.validMountainArray([0,3,2,1])