# Leetcode 991. Broken Calculator

class Solution:
    def brokenCalc(self, X, Y):
        # Solution 1. No recursion
        ans = 0
        while Y > X:
            ans += 1
            if Y%2: Y += 1
            else: Y //= 2

        return ans + X-Y

        # Solution 2. Recursion, better than 99% of submissions
        """
        if X > Y: return X - Y
        if X == Y: return 0
        if Y % 2 == 0:
            return self.brokenCalc(X, Y//2) + 1
        else:
            return self.brokenCalc(X, Y + 1) + 1
        """
        # My solution below - doesn't work
        """
        steps = 0
        def calc(input, match, steps):
            if input == match:
                return steps
            else:
            #while input != match and input < match and input >= 0 and input != match:
                while input < match and input >= 0:
                #     if calc(input * 2, match) == match:
                #         return input

                #     if calc(input - 1, match) == match:
                #         return input
                # return input
                    return calc(input * 2, match, steps + 1)
                    return calc(input - 1, match, steps + 1)
                #return steps
        print(calc(X, Y, steps))
        #return input
        """



Run = Solution()
Run.brokenCalc(1024, 1)
(5, 8)