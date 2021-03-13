# Leetcode 1784. Check if Binary String Has at Most One Segment of Ones

class Solution:
    def checkOnesSegment(self, s):
        counter = False
        for i in s:
            if i == "0":
                counter = True
            if counter and i == "1":
                return False
        return True

Run = Solution()
Run.checkOnesSegment("110")