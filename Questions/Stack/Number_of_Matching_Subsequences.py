# Leetcode 792. Number of Matching Subsequences

# 1. Create a dict of all words with key = string & value = list,
# the first letter of each word is the key
# 2. Iterate through each character in S
# 3. For each character, lookup the dictionary for the list of words
# starting with that char
# 4. Reset the value of the list of words to an empty list
# 5. Iterate through the list of words retrieved in step 3
# if the word is a single letter increment count because we have found a subsequence
# Otherwise, slice off the first character and add the sliced word back to the dictionary
# This time, it is added to the entry for which the key is equal to the first letter of the sliced word.

import sys
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s, words):

        memo = defaultdict(list)
        count = 0
        for word in words:
            memo[word[0]].append(word)
        for char in s:
            words_expecting_char = memo[char]
            memo[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    count += 1
                else:
                    memo[word[1]].append(word[1:])

        print(memo)


Run = Solution()
Run.numMatchingSubseq("abcde", ["a","bb","acd","ace"])