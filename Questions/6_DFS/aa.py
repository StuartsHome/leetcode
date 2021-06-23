class Solution:
    def numMatchingSubseq(self, s, words):
        
        
        result = []
        words = sorted(words, key=len)
        def helper(word):
            a = 0
            b = 0
            while a < len(word) and b < len(s):
                if s[b] == word[a]:
                    a += 1
                b += 1
            if a >= len(word):
                result.append(word)
        N = len(s)
        for i in words:
            if len(i) < s:
                helper(i)
            else:
                break
        return result

Run = Solution()
Run.numMatchingSubseq("abcde",["a","bb","acd","ace"])