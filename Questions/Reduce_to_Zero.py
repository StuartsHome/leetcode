# Leetcode ?. Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps(self, num):

        steps = 0
        temp_num = num
        while temp_num > 0:
            if temp_num % 2 == 0:
                temp_num /= 2
            else:
                temp_num -= 1
            steps += 1
        print(steps)



Run = Solution()
Run.numberOfSteps(123)




