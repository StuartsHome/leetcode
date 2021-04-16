class Solution:
    def removeDuplicates(self, s, k):
        total = len(s)
        copy_s = s
        prev = s[0]
        counter = 1
        while total:
            for i in range(len(copy_s)):
                if copy_s[i] == prev:
                    counter += 1
                    if counter == k:
                        copy_s = copy_s[:i-(counter)] + copy_s[i + 1:]
                        total -= k
                        counter = 0
                        break
                else:
                    counter = 1
                prev = s[i]

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