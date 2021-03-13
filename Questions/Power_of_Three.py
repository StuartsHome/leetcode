
class Solution:
    def isPowerOfThree(self, n):
        # Solution from Discussions

        # One simple way of finding out if a number n is a power of a number b is to keep
        # dividing n by b as long as the remainder is 0.
        # Hence it should be possible to divide n by b, x times, every time with a remainder
        # of 0 and at the end the result to be 1.

        # Notice that we need a if statement to check that n != 0, othrwise the while loop will never
        # finish. For negative numbers, the algorithm does not make sense, so we will include this condition
        # as well.

        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1


        # Solution from Geeks for Geeks
        """
        y = 3
        pow = 1
        while pow < n:
            pow = pow * y
        print(pow == n)
        """

Run = Solution()
Run.isPowerOfThree(35)
(27)