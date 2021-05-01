from itertools import product
class WordFilter:
    def __init__(self, words):
        self.d = {}
        # def prod(*args, repeat=2):
        #     pools = [tuple(pool) for pool in args] * repeat
        #     result = [[]]
        #     for pool in pools:
        #         result = [+[y] for x in result for y in pool]
        #     for prod in result:
        #         yield tuple(prod)
                
        for i, word in enumerate(words):
            for p, s in product(range(len(word) + 1), repeat=2):
                self.d[word[:p], word[s:]] = i
        print(self.d)
    def f(self, prefix, suffix):
        return self.d.get((prefix, suffix), -1)

Run = WordFilter(["cabaabaaaa","ccbcababac"])
# Run.f("a","aa")
# ( ["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"])