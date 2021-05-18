# Leetcode 395. Longest Substring with At Least K Repeating Characters
class Solution:
    def longestSubstring(self, s, k):
        memo = {}
        result = {}
        for x in s:
            if x in memo:
                memo[x] += 1
            else:
                memo[x] = 1
        result = {x:k for x,i in memo.items() if i >= k}
        copy = result.copy()
        sub = ""
        total = 0
        for i in s:
            if i in copy:
                copy[i] -= 1
                sub += i
                if sum(copy.values()) == 0:
                    total = max(total, len(sub))
            else:
                sub = ""
                copy = result.copy()
        # return total
        print(total)
        


Run = Solution()
Run.longestSubstring("bbaaacbd",3)
("ababacb", 3)
("aaabb", 3)


"""
        if len(s) < k: return 0
        c = Counter(s)
        st = 0
        for p, v in enumerate(s):

            if c[v] < k:

                return max(self.longestSubstring(s[st:p],k), self.longestSubstring(s[p+1:],k))

        return len(s)
"""