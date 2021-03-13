# Leetcode 820. Short Encoding of Words
class Solution:
    def minimumLengthEncoding(self, words):
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good) # +1 for the ending hash

Run = Solution()
Run.minimumLengthEncoding(["time", "me", "bell", "ll"])