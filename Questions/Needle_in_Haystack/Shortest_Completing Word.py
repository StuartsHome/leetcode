# Leetcode 748. Shortest Completing Word

class Solution:
    def shortestCompletingWord(self, licensePlate, words):    
        result = ''.join([i for i in licensePlate if not i.isdigit()])
        result = result.lower()
        result = result.replace(" ", "")
        result2 = []
        for i in words:
            copy = list(result)
            for j in i:
                if j in copy:
                    #ind = copy.index(j)
                    copy.remove(j)
            #if not copy:
            if len(copy) == 0:
                result2.append(i)
        return min(result2 , key=len)


Run = Solution()
Run.shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"])
("1s3 456", ["looks","pest","stew","show"])