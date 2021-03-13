# Leetcode ?. Letter Case Permutation

class Solution:
    def letterCasePermutation(self, S):
        res = ['']
        for ch in S:
            tmp = []
            for i in res:
                if ch.isalpha():
                    tmp.append(i + ch.upper())            
                    tmp.append(i + ch.lower())
                else:
                    tmp.append(i + ch)
            res = tmp
        return res

        # Backtracking process including List Comprehensions
        """
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res
        """

                

Run = Solution()
Run.letterCasePermutation("a1b2")