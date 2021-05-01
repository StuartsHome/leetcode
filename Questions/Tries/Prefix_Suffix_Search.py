# Leetcode 745. Prefix and Suffix Search
# For each word we generate all prefix and suffix pairs and put them into a dictionary


from itertools import product
class WordFilter:
    def __init__(self, words):
        self.memo = {}
        for i, word in enumerate(words):
            for p, s in product(range(len(word) + 1), repeat=2):
                self.memo[word[:p], word[s:]] = i

    def f(self, prefix, suffix):
        return self.memo.get((prefix, suffix), -1)


Run = WordFilter( ["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"])
# (["Apple"])
# Run.f("a", "e")
Run.f("a","aa")
("ab","abcaccbcaa")
("cabaaba","abaaaa")
("cacc","accbbcbab")
("ccbcab","bac")

("bccbacbcba","a")
# ("a", "e")


["bac","cba"]
["ac","accabaccaa"]
["bcbb","aa"]
["ccbca","cbcababac"]


class Trie():
    def __init__(self):
        self.memo = {}
        self.index = 0
    def insert(self, word, index): 
        curr = self.memo
        curr.index = index
        for char in word:
            if char not in curr:
                curr[char] = {}
                curr[char].index = index
            curr = curr[char]
        curr["!"] = True

    def startsWith(self, word):
        curr = self.memo
        for char in word:
            if char not in curr:
                return -1
            curr = curr[char]
        return curr.index

class WordFilter:
    def __init__(self, words):
        self.trie = Trie()
        self.words = {}

        def product(*args, repeat=2):
            pools = [tuple(pool) for pool in args] * repeat
            result = [[]]
            for pool in pools:
                result = [+[y] for x in result for y in pool]
            for prod in result:
                yield tuple(prod)

        for index, word in enumerate(words):
            long = word + "#" + word
            for i in range(len(word)):
                self.trie.insert(long[i:], index)

    def f(self, prefix, suffix):
        return self.trie.startsWith(suffix + "#" + prefix)
