# Leetcode 1437. Check if All 1's Are at Least Length K Places Away



class Solution:
    def kLengthApart(self, nums, k):
        counter = k
        #boo = False
        for i in nums:
            if i == 0:
                counter += 1
            else:
                if counter < k: #and boo:
                    print("False")
                counter = 0
            boo = True
        print("True")


Run = Solution()
Run.kLengthApart([1,0,0,0,1,0,0,1], 2)

([1,1,1,1,1], 0)