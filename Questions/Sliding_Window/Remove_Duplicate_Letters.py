# Leetcode 316. Remove Duplicate Letters

from collections import Counter
# import string
class Solution:
    def removeDuplicateLetters(self, s):
        last_occ = {num: indx for indx, num in enumerate(s)}

        stack = ["!"]
        visited = set()
        
        for ind, val in enumerate(s):
            if val in visited: continue

            while val < stack[-1] and last_occ[stack[-1]] > ind:
                visited.remove(stack.pop())
            stack.append(val)
            visited.add(val)
        return "".join(stack[1:])



Run = Solution()
Run.removeDuplicateLetters("cbacadcbc")
("bcabc")
        # d = {chr(i+96):i for i in range(1,27)}
        # minner = 97
        # memo = {}
        # for key, i in enumerate(s):
        #     if d[i] <= minner:
        #         minner = d[i]
        #         if i in memo:
        #             aa = memo[i].append(key)
        #             # aa = aa.append(key)
        #             memo[i] = aa
        #         else:
        #             memo = {i: [key]}
        # print(memo)
        
        # j = curr = 0
        # result = []
        # for i in range(len(s)):
        #     counter = i
        #     memo_2 = [[counter]]
        #     for j in range(i, len(s)):
        #         if s[j] not in memo_2:
        #             memo_2.append(s[j])
        #         else:
        #             bb = memo_2.copy()
        #             result.append(bb)
        #             aa = memo_2.count(s[j])
        #             while memo_2 and memo_2.count(s[j]) > 0:
        #                 memo_2.pop(0)
        #             memo_2.append(s[j])
            
        # print(result)