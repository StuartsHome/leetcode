
# Leetcode 781. Rabbits in Forest
from collections import Counter
class Solution:
    def numRabbits(self, answers):

        intt1 = "00000000000000000000000000001011"
        
        print(intt1)
        for i in intt1:
            if i == "1":
                print(i)
        #for i in intt1:
        #    print(i)



        # Answer taken from discussions
        c = Counter()
        """
        result = 0
        for i in answers:
            if c[i] % (i + 1) == 0:
                result += i + 1
            c[i] += 1
        print(result)
        """
        # My answer that does not work !!!!
        """
        memo = {}
        total1 = 0
        total2 = len(answers)
        for i in answers:
            if i in memo:
                if memo[i] == 0:
                    memo[i] += 1
                else:
                    memo[i] -= 1
                total1 += 1
            else:
                memo[i] = 1
                

        for i in memo:
            if memo[i] > 0:
                total2 += (i * memo[i]) - (len(answers) - total1)
        print(total2)
        """

Run = Solution()
Run.numRabbits([1, 1, 2])

([10,10,10])














([1, 1, 2])

