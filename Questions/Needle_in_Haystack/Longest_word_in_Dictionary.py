# Leetcode 524. Longest Word in Dictionary through Deleting

class Solution():
    def findLongestWord(self, s, d):
        # Lambda sorts by the length of the word
        # If two words of same length, they are sorted Lexicographically, i.e. alphabetically

        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i = 0
            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1
            if i == len(word):
                return word
        return ""


Run = Solution()
Run.findLongestWord("abpcplea", ["a","b","c"])

("bab", ["ba","ab","a","b"])

("abpcplea", ["a", "b", "c"])
("abpcplea", ["ale","apple","monkey","plea"])