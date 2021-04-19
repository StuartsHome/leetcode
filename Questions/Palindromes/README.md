# Palindromes
When doing palindromes, I like to go from center to each end!

We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only `2n - 1` such centers.

You might be asking why there are `2n - 1` but not nn centers? The reason is the center of a palindrome can be in between two letters. Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's.

- Time complexity : O(n^2). 
Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).
- Space complexity : O(1). - Constant Space.
My words: you have to loop through each element which is O(N), and for every element you\
may have to loop again which is O(N^2)

NOTE - Manacher's Algorithm does it in O(N) - Linear time, but non trivial.

- Manacher's - O(N)
- My solutions are at worst - O(n^2)
- Other solutions are O(n^3): two for loops to traverse each element twice, then while loop to expand from center
### Palindromic Substrings - Time Complexity O(n^2) - Space O(1)
```python
class Solution():
    def longestPalindrome(self, s):
        total = 0
        def helper(l,r):
            aa = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                aa += 1
                l -= 1
                r += 1
            return aa
                
        N = len(s)
        for i in range(N):
            total += helper(i, i)
            total += helper(i, i + 1)
        return total              
Run = Solution()
Run.longestPalindrome("aaa")
```

## Longest Palindromic Substring - Time Complexity O(n^2) - Space O(1)
```python
class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        print(res)

    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

Run = Solution()
Run.longestPalindrome("cbbd")
```
## Refactored using Max function
```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)

        return res
       
        
    def helper(self,s,l,r):
        
        while 0<=l and r < len(s) and s[l]==s[r]:
                l-=1; r+=1
        return s[l+1:r]
```