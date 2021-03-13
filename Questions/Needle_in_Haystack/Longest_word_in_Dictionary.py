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

        # My solution - doesn't work
        """
        result = []
        longest = ""
        for i in range(len(d)):
            last_index = -1
            flag = True
            for j in range(len(d[i])):
                if d[i][j] in s and j > last_index:
                #print(j, d[i][j])
                    if j <= last_index:
                        break
                    else:
                        last_index = j
                else:
                    flag = False
                    break
            if flag: 
                if len(d[i]) >= len(longest):
                    if len(d[i]) == len(longest):
                        if d[i] < longest:
                            longest = d[i]
                    else:
                        longest = d[i]
                result.append(d[i])
        print(result, longest)
        """
            



Run = Solution()
Run.findLongestWord("abpcplea", ["a","b","c"])

("bab", ["ba","ab","a","b"])

("abpcplea", ["a", "b", "c"])
("abpcplea", ["ale","apple","monkey","plea"])