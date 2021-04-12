# Leetcode 1249. Minimum Remove to Make Valid Parentheses

class Solution:
    def minRemoveToMakeValid(self, s):
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)



Run = Solution()
Run.minRemoveToMakeValid("))(()")
("(a(b(c)d)")

("lee(t(c)o)de)")