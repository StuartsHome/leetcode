# Leetcode 1023. Camelcase Matching

class Trie:
    def __init__(self):
        self.memo = {}
        
    def insert(self, words):
        curr = self.memo
        for char in words:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['#'] = True
            
    def search(self, words):
        curr = self.memo
        for char in words:
            if not char in curr and char.isupper():
                return False
            elif char in curr:
                curr = curr[char]
        if '#' in curr:
            return True
        return False
            
                
class Solution:
    def camelMatch(self, queries, pattern):
        t = Trie()
        t.insert(pattern)
        memo = []
        for word in queries:
            if t.check(word):
                memo.append(True)
            else:
                memo.append(False)
        return memo

        # Non trie needle haystack solution
        """
    def camelMatch(self, queries, pattern):
        def patternMatch(p, q):
            i = 0
            for j, c in enumerate(q):
                if i < len(p) and p[i] == c:
                    i += 1
                elif c.isupper():
                    return False
            return i == len(p)
        return [patternMatch(pattern, q) for q in queries]
    
        """

Run = Solution()
Run.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB")