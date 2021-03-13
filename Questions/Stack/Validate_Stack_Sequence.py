# Leetcode 946. Validate Stack Sequence

# Description:
# For each value, push it to the stack
# Then, greedily pop values from the stack if they are the next values to pop.
# At the end, we check if we have popped all the values sucessfully

class Solution:
    def validateStackSequence(self, pushed, popped):
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            target = stack[-1]
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)    # J is only incremented when a value if popped from stack


        # Slower
        """
        n = len(pushed)
        if n < 2:
            return True
        stack = []
        j = 0
        for i in pushed:
            stack.append(i)
            while stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1
        print(j == n)
        """

Run = Solution()
Run.validateStackSequence([1,2,3,4,5], [4,5,3,2,1])


([1,2,3,4,5], [4,3,5,1,2])


