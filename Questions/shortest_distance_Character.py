# Leetcode 821. Shortest Distance to a Character


class Solution:
    def shortestToChar(self, s, c):

        totals = []

        for i in range(len(s)):
            j,t = i, i
            result = set()
            while j < len(s) - 1 and s[j] != c:
                j += 1
            if s[j] == c:
                result.add(j - i)
            while t > 0 and s[t] != c:
                t -= 1
            if s[t] == c:
                if (i - t) >= 0:
                    result.add(i - t)
            totals.append(min(result))
        print(totals)

    

Run = Solution()
Run.shortestToChar("aaba", "b")
("aaab", "b")

("loveleetcode", "e")
