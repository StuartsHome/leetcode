# 1704. Determine if String Halves Are Alike

class Solution:
    def halvesAreAlike(self, s):
        s = s.lower()
        N = len(s)
        half = N//2
        i,j = half - 1,half
        a = 0
        b = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        while i >= 0 and j <= N:
            if s[i] in vowels:
                a += 1
            if s[j] in vowels:
                b += 1
            i -= 1
            j += 1
        if a == b:
            return True
        return False


Run = Solution()
Run.halvesAreAlike("AbCdEfGh")
("book")

