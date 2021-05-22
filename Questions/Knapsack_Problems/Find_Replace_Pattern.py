# Leetcode 890. Find and Replace Pattern
# Similar to Leetcode 205. Isomorphic Strings

# Solution 1: T: O(n * k), S: O(n * k)
    # n is the number of words, and K is the length of each word
# Solution 2: T: O(n * k), S: O(n * K)

# Filter() -> Returns an itertor were the items are filtered through a function
# filter(function, iterator)
# Basically the function runs for each item in iterator

# Setdefault() -> Returns the value of the item with the specified key
# if the key does not exist, insert the key, with the specified value.
# dictionary.setdefault(keyname, value)


# Use set default for frequency table that doesn't update like:
# "abb" -> [0, 1, 1]

class Solution:
    def findAndReplacePattern(self, words, pattern):
        # def match(word):
        #     P = {}
        #     for x, y in zip(pattern, word):
        #         if P.setdefault(x, y) != y:
        #             return False
        #     return len(set(P.values())) == len(P.values())

        # result = []
        # for i in words:
        #     aa = match(i)
        #     if aa:
        #         result.append(i)
        # print(result)

        def f(w):
            memo = {}
            return [memo.setdefault(c, len(memo)) for c in w]
        fp = f(pattern)
        # return [w for w in words if f(w) == fp]
        result = []
        for w in words:
            aa = f(w)
            if aa == fp:
                result.append(w)
        return result

Run = Solution()
Run.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb")

        # # Two maps
        # def match(word):
        #     m1, m2 = {}, {}
        #     for w, p in zip(word, pattern):
        #         if w not in m1: m1[w] = p
        #         if p not in m2: m2[p] = w
        #         if (m1[w], m2[p]) != (p, w):
        #             return False
        #     return True

        # # This can be replaced with a for loop
        # return filter(match, words)

        # """
        # result = []
        # for i in words:
        #     aa = match(i)
        #     if aa:
        #         result.append(i)
        # return result
        # """