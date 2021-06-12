# Leetcode 316. Remove Duplicate Letters
# Greedy w/ stack
# T: O(n)
# S: O(26) - because it will be the longest size of our stack and answer.


# The key information this approach is knowing where the last occurrence of each character is.
# Everything before the first last occurrence is a candidate for deletion.

class Solution:
    def removeDuplicateLetters(self, s):
        last_occ = {num: indx for indx, num in enumerate(s)}    # to find the last index of each letter in s
        result = ""
        for ind, val in enumerate(s):
            if val not in result:
                while val < result[-1:] and ind < last_occ[result[-1]]:
                    result = result[:-1]
                result += val
        return result

        # last_occ = {num: indx for indx, num in enumerate(s)}    # to find the last index of each letter in s

        # stack = ["!"]
        # visited = set()
        
        # for ind, val in enumerate(s):
        #     if val in visited: continue

        #     while val < stack[-1] and last_occ[stack[-1]] > ind:
        #         visited.remove(stack.pop())
        #     stack.append(val)
        #     visited.add(val)
        # return "".join(stack[1:])

Run = Solution()
Run.removeDuplicateLetters("cbacadcbc")
("bcabc")