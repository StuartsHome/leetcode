# Leetcode 395. Longest Substring with At Least K Repeating Characters
# Good video: https://www.youtube.com/watch?v=bHZkCAcj3dc&ab_channel=KnowledgeCenter
# Good explanation: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/753840/Python-Solution-from-Youtube-tutorial-Not-a-medium-question-for-sure-For-Interviews

# Create count > n
# Linear scan > n
# Space > O(N)


from collections import defaultdict
class Solution:
    def longestSubstring(self, s, k):
        # Recursion - Understandable
        if k > len(s) or len(s) == 0:
            return 0
        if k <= 1:
            return len(s)
        memo = {}
        for char in s:
            memo[char] = memo.get(char, 0) + 1
        
        left = 0
        while left < len(s) and memo[s[left]] >= k:
            left += 1
        if left >= len(s) - 1:
            return left
        
        substringLeft = self.longestSubstring(s[:left], k)

        while left < len(s) and memo[s[left]] < k:
            left += 1
        
        substringRight = self.longestSubstring(s[left:len(s)], k) if left < len(s) else 0
        return max(substringLeft, substringRight)

        # Brute Force - Really Slow
        """
        def build(start, s, k):
            memo, valid, last = {}, set([]), -1
            for i in range(start, len(s)):
                memo[s[i]] = memo.get(s[i], 0) + 1
                if memo[s[i]] and memo[s[i]] >= k:
                    valid.add(s[i])
                if len(memo) == len(valid):
                    last = i

            return 0 if last == -1 else last-start+1

        total = 0
        for j in range(len(s)):
            total = max(total, build(j, s, k))
        return total
        """

        # Brute Force - using Default Dict
        """
        def build(start, s, k):
            fmap, valid, last = defaultdict(int), set([]), -1
            for i in range(start, len(s)):
                fmap[s[i]] += 1
                if fmap[s[i]] >= k:
                    valid.add(s[i])
                if len(fmap) == len(valid):
                    last = i
            return 0 if last == -1 else last-start+1

        total = 0
        for i in range(len(s)):
            total = max(total, build(i, s, k))
        print(total)
        """

Run = Solution()
Run.longestSubstring("bbaaacbd",3)
("ababacb", 3)
("aaabb", 3)

# Recursion
"""
if len(s) < k: return 0
c = Counter(s)
st = 0
for p, v in enumerate(s):

    if c[v] < k:

        return max(self.longestSubstring(s[st:p],k), self.longestSubstring(s[p+1:],k))

return len(s)
"""     

# Brute Force
"""
maxi=0
for i in range(len(s)):
    check=set()
    table=defaultdict(int)
    for j in range(i, len(s)):
        table[s[j]]+=1
        if table[s[j]]>=k:
            check.add(s[j])
        if len(check)==len(table):
            maxi=max(maxi, j-i+1)
return maxi

"""









# Frequency Counter
# Dictionary instead of Counter
"""
for char in s:
    hashmap[char] = hashmap.get(char, 0) + 1
"""