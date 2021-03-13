# Leetcode 856. Score of Parentheses

class Solution:
    def scoreOfParentheses(self, S):
        # Both solutions are very good!
        """
        # 1. Divide and Conquer
        def F(i, j):
            #Score of balanced string S[i:j]
            ans = bal = 0

            #Split string into primitives
            for k in range(i, j):
                bal += 1 if S[k] == '(' else -1
                if bal == 0:
                    if k - i == 1:
                        ans += 1
                    else:
                        ans += 2 * F(i+1, k)
                    i = k+1

            return ans

        return F(0, len(S))
        """

        # 2. Stack
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()
	
p1 = Solution()
p1.scoreOfParentheses("(()(()))")

("(({}))")