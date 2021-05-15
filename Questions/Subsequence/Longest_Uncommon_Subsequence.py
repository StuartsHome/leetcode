# Leetcode 521. Longest Uncommon Subsequence I

class Solution:
    def findLUSlength(self, a, b):
        N = len(a)
        B = len(b)
        if N == B:
            if a in b:
                return -1
        return max(N, B)

Run = Solution()
Run.findLUSlength("horbxeemlgqpqbujbdagizcfairalg",
"iwvtgyojrfhyzgyzeikqagpfjoaeen")


("aweffaf", "aweffaf")
("aefawfawfawfaw","aefawfeawfwafwaef")