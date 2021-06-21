# Leetcode 680. Valid Palindrom II
# T: O(n)
# S: O(n) - list slices each create new strings

# Info:
# This works because only one element can be removed to make it a valid palindrome.
# With two pointers at either end of the array, if they are the same element
# reduce the window and try again.
# When the values are different, try removing at either end to make it a valid palindrome.
# If removing at either end doesn't make a valid palindrome, it means it will require > 1+ removals to 
# make it a valid palindrome, so return False.

class Solution:
    def validPalindrome(self, s):

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                delete_right, delete_left = s[left:right], s[left + 1: right + 1]
                return  delete_right == delete_right[::-1] or delete_left == delete_left[::-1]
            left, right = left + 1, right - 1
        return True
# Run = Solution()
# Run.validPalindrome("yyaappiyy")
# ("eccer")
# ("abca")


# Recursive - To answer the question of: If more than 1 element can be removed to make valid palindrome
# We no longer need to compare correct and reversed, because
# The base condition "if removals == 0:" tells you, if you have have no removals left
# return False, else 

class Solution:
    def validPalindrome(self, s):
        # T: ?, S: O(n)
        def dfs(s, removals):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    if removals == 0:
                        return False
                    delete_r, delete_l = dfs(s[l:r], removals - 1), dfs(s[l + 1:r + 1], removals - 1)
                    return delete_r or delete_l
                l += 1
                r -= 1
            return True
        return dfs(s, 1)

        # or T: O(n), S: O(1) - no string slicing
        def dfs_2(l, r, removals):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if removals == 0:
                        return False
                    del_r, del_l = dfs_2(l + 1, r, removals - 1), dfs_2(l, r - 1, removals - 1)
                    return del_r or del_l
            return True
        return dfs_2(0, len(s) - 1, 1)



Run = Solution()
Run.validPalindrome("yypaapiyy")
("eccer")
("abca")