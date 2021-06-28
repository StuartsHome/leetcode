# Leetcode 1209. Remove ALl Adjacent Duplicates in String II

class Solution:
    def removeDuplicates(self, s, k):
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)

        # Solution 2 - More verbose
        stack = [["!", 1]]
        for elem in s:
            if elem == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([elem, 1])
            
            while stack[-1][1] >= k:
                stack[-1][1] -= k
                if stack[-1][1] == 0: stack.pop()
             
        return "".join(i*j for i, j in stack[1:])





    # This works, but returns a TLE on test case 18/19
        # s = list(s)
        # stack = [[s[0],0]]
        # counter = 1
        # i = 1
        # while i < len(s):
        #     if s[i] == stack[-1][0]:
        #         stack.append([s[i],i])
        #         counter += 1
        #         if counter == k:
        #             while stack:
        #                 val, ind = stack.pop()
        #                 s.pop(ind)
        #             i = 1
        #             counter = 1
        #             if s:
        #                 stack = [[s[0],0]]
        #         else:
        #             i += 1  
        #     else:
        #         stack = [[s[i],i]]
        #         counter = 1
        #         i += 1
        # return "".join(s)








Run = Solution()
Run.removeDuplicates("deeedbbcccbdaa", 3)













"""
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)
        """