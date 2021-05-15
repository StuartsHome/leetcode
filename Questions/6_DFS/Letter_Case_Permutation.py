# Leetcode 784. Letter Case Permutation

class Solution:
    def letterCasePermutation(self, S):
        # Slow - Similar to permutations (easy to remember)
        result = []
        def dfs(ind, path):
            if not ind and len(path) == len(S) and path not in result:
                result.append("".join(path))
            for i in range(len(ind)):
                if ind[i].isalpha():
                    aa = ind[i].lower()
                    dfs(ind[i + 1:], path + [aa])
                    aa = ind[i].upper()
                    dfs(ind[i + 1:], path + [aa])
                else:
                    dfs(ind[i + 1:], path + [ind[i]])
        dfs(S, [])
        print(result)

        # Faster - DFS
        result = []
        def dfs(ind, path):
            if len(path) == len(S):
                result.append("".join(path))
            else:
                if S[ind].isalpha():
                    dfs(ind + 1, path + [S[ind].swapcase()])
                dfs(ind + 1, path + [S[ind]])
        dfs(0, [])
        return result
        
        # Fast
        result = []
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

# class Solution:
#     def letterCasePermutation(self, S):
        



# Run = Solution()
# Run.letterCasePermutation("a1b2")