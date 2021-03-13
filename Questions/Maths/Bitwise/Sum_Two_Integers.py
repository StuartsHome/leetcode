# Leetcode 371. Sum of Two Integers

class Solution:
    def getSum(self, a, b):
        mask = 0xFFFFFFFF
        while b != 0:
            #a, b = (a ^ b) & mask, ((a & b) << 1) & mask // replaced with two lines and temp variable to better explain the code
            temp = a
            a = (a ^ b) & mask
            b = ((a & b) << 1) & mask 
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a


        # Doesn't work because Python uses arbitrary length integer
        # causes infinite loop, needs to stop at max
        """
        while b != 0:
            data = a & b
            a = a ^ b
            b = data << 1
        print(a)
        """


        # Not Legal - sum is another form of +
        """
        list = [a,b]
        return sum(list)
        """

Run = Solution()
Run.getSum(1, 2)