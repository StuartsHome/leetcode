# Leetcode 906. Super Palindromes
# Leetcode Hard

class Solution:
    def superpalindromesInRange(self, left, right):
        count = 0
        nums = [x for x in range(int(left), int(right) + 1)]
        for i in nums:
            if str(i) == str(i)[::-1]:
                aa = int(i) ** .5
                if aa % 1 == 0:
                    aa = int(aa)
                    if str(aa) == str(aa)[::-1]:
                        count += 1
        return count
Run = Solution()
Run.superpalindromesInRange("4", "1000")