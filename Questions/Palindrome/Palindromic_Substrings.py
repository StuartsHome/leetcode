# Leetcode ?. Palindromic Substrings

# Each element in the array is visited twice
# Right is +1 ahead of left, for once every two turns, left and right are at the same index
# From each element we center expand, left and right

# Left and right values:
# Left: 0 // 2 = 0      Right = (0 + 1) // 2 = 0
# Left: 1 // 2 = 0      Right = (1 + 1) // 2 = 0
# Left: 2 // 2 = 1      Right = (2 + 1) // 2 = 1
# Left: 3 // 2 = 1      Right = (3 + 1) // 2 = 1
# Left: 4 // 2 = 2      Right = (4 + 1) // 2 = 2
# Left: 5 // 2 = 2      Right = (5 + 1) // 2 = 2
# Left: 6 // 2 = 3      Right = (6 + 1) // 2 = 3


from itertools import permutations
class Solution:
    def countSubstrings(self, s):
        N = len(s)
        result = 0

        for i in range(2 * N - 1):
            left = i // 2
            right = (i + 1) // 2
            while left >= 0 and right < N and s[left] == s[right]:
                result += 1
                left -= 1
                right  += 1
        return result

    # Similar method - but not using (2 * N - 1)
    """
    def countSubstrings(self, S):
        for i in range(len(s)):
            for j in range(2):
                left = i
                right = left + j

                while left >= 0 and right < len(s) and S[left] == S[right]:
                    ans += 1
                    left -= 1
                    right += 1
        return ans
    """
Run = Solution()
Run.countSubstrings("level")

("aaa")
("abc")