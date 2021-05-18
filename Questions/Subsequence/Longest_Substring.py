# Leetcode 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s):

        total = 0
        substring = ""
        for i in s:
            if i not in substring:
                substring += i
                total = max(total, len(substring))
            else:
                cut = substring.index(i)
                substring = substring[cut+1:] + i
        return total
        
Run = Solution()
Run.lengthOfLongestSubstring("pwwkew")

("abcabcbb")
"""
    max_len = 0
        for i in range(len(s)):
            memo = set()
            result = ""
            j = i
            while j < len(s) and s[j] not in memo:
                if s[j] in memo:
                    max_len = max(max_len, len(result))

                else:
                    memo.add(s[j])
                    result += s[j]
                j += 1
            max_len = max(max_len, len(result))    
        print(max_len)"""