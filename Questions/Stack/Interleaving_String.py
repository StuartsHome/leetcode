# Leetcode 97. Interleaving String
from collections import deque
class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        last = set([(0,0)]) # Has to be 3 sets of brackets, 2 doesn't work

        for char in s3:
            current = set()
            for i, j in last:   # Each iteration, char has to match at least i or j
                if i < len(s1) and s1[i] == char:
                    current.add((i + 1, j))
                if j < len(s2) and s2[j] == char:
                    current.add((i, j + 1))
            if not current:
                return False
            last = current
        return True


        """
        # DP w/ LRU cache
        M = len(s1)
        N = len(s2)
        
        @lru_cache()
        def dfs(i, j, k):
            if i > M-1 and j > N-1:
                return True
            if i < M and s1[i] == s3[k] and dfs(i + 1, j, k + 1):
                return True
            if j < N and s2[j] == s3[k] and dfs(i, j + 1, k + 1):
                return True
            return False
        return Counter(s1) + Counter(s2) == Counter(s3) and dfs(0,0,0)
        """

Run = Solution()
Run.isInterleave("aabc","abad","aabcabad")
("aa","ab","aaba")
("","","a")
("aabcc", "dbbca", "aadbbcbcac")


        # if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
        #     return True
        
        # stack1 = deque(s1)
        # stack2 = deque(s2)
        
        # for i in s3:
        #     top1 = stack1.popleft() if stack1 else None
        #     top2 = stack2.popleft() if stack2 else None
        #     # top1 = stack1.popleft()
        #     # top2 = stack2.popleft()
        #     if i != top1 and i != top2:
        #         return False
        #     if i == top1:
        #         stack2.appendleft(top2)
        #     elif i == top2:
        #         stack1.appendleft(top1)
        # if not top1 and not top2:
        #     return True

