


# Leetcode 5. Longest Palindromic Substring



class Solution:
    def longestPalindrome(self, s):


        # The code below doesn't work
        """
        #rev_s = ""
        rev_s = ""
        copy_s = s
        word = ""
        #counter_totals = []
        counter_totals = {}
        #counter_totals = set()
        
        for i in s[::-1]:
            rev_s += i

        for i in range(len(rev_s)):
            word = s[i]
            counter = i
            while counter < len(rev_s) -1  and rev_s.find(word) != -1:
                counter += 1
                word += s[counter]

            counter_totals[len(word[:len(word)-1])] = word[:len(word)-1]
        aa = max(counter_totals)
        print(counter_totals[aa])
        """

        # The code below works - and was taken from discussions
    def longestPalindrome(self, s: str) -> str:
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

("babad")
        
        
        
   