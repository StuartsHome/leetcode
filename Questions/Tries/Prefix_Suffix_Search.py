# Leetcode 745. Prefix and Suffix Search


class WordFilter:
    def __init__(self, words):
        self.memo = words

    def f(self, prefix, suffix):
        curr = self.memo
        for ind, val in enumerate(curr):
            aa = val.lower()
            if aa.startswith(prefix) and aa.endswith(suffix):
                return ind
        return -1
            


Run = WordFilter([["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]])
# (["Apple"])
# Run.f("a", "e")
Run.f("a", "e")
["bccbacbcba","a"]
["ab","abcaccbcaa"]
["a","aa"]
["cabaaba","abaaaa"]
["cacc","accbbcbab"]
["ccbcab","bac"]
["bac","cba"]
["ac","accabaccaa"]
["bcbb","aa"]
["ccbca","cbcababac"]
