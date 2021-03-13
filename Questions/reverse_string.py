# Leetcode 344 - Reverse String

class Solution:
    def reverseString(self, s):
        #for i in s:
        #    print(i)

        """
        s = "".join(s)
        temp = s
        reverseNum = 0
        while temp != 0:
            reverseNum = (reverseNum * 10) + (temp % 10)
            temp = temp // 10
        print(reverseNum)
        """
        """
        rev = []
        for i in s[::-1]:
            rev.append(i)
        print(rev)
        """
        i = 0
        j = len(s)-1
        
        while i <= j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        print(s)

Run = Solution()
Run.reverseString(["H","a","n","n","a","h"])


(["h", "e", "l", "l", "o"])