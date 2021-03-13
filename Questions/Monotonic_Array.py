# Leetcode 896. Monotonic Array

class Solution:
    def isMonotonic(self, A):
        i,j = 0,0
        catch = True
        
        #for i in range(len(A)-1):
        while i < len(A) -1:
            if A[i] == A[i + 1]:
                while i < len(A) -1 and A[i] == A[i + 1]:
                    i += 1

            elif catch and A[i] <= A[i + 1]:
                while i < len(A) -1 and A[i] <= A[i + 1]:
                    i += 1
                    catch = False
                
            elif catch and A[i] >= A[i + 1]:
                while i < len(A) -1 and A[i] >= A[i + 1]:
                    i += 1
                    catch = False
            else: 
                return False
        return True 

        # Code below from discussions
        # Slower than my implimintation, but easier to read
        """
        increasing = decreasing = True

        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False

        return increasing or decreasing
        """




Run = Solution()
Run.isMonotonic([1,1,0])
([1,3,2])
([6,5,4,4])
([1,2,2,3])