

class Solution:
    def isAnagram(self, s, t):

        # Better runtime than below - my submission from Sep 19th
        if len(s) != len(t):
            return False
        memo = {}
        for i in s:
            if i in memo:
                memo[i] = memo[i]+1
            else:
                memo[i] = 1
        for i in t:
            if i in memo:
                if memo[i] > 0:
                    memo[i] = memo[i] -1
                else:
                    return False
            else:
                return False
        return True


        # Slower runtime - My Code - Feb 11th
        """
        memo = {}
        for i in s:
            if i in memo:
                memo[i] += 1
            else:
                memo[i] = 1
        for i in t:
            if i in memo:
                if memo[i] == 1: memo.pop(i, False)
                else:
                    memo[i] -= 1
            else:
                return False
        print(len(memo))
        if len(memo) > 0:
            return False
        return True
        """
Run = Solution()
Run.isAnagram("anagram", "nagaram")
("ab", "b")
("rat", "car")

