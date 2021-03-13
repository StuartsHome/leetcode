# 1649. Create Sorted Array through Instructions

class Solution:
    def createSortedArray(self, instructions):
        m = max(instructions)
        c = [0] * (m + 1)

        def update(x):
            while (x <= m):
                c[x] += 1
                x += x & -x

        def get(x):
            result = 0
            while (x > 0):
                result += c[x]
                x -= x & -x
            return result

        result = 0
        for i, a in enumerate(instructions):
            result += min(get(a - 1), i - get(a))
            update(a)
        print(result % (10**9 + 7))



Run = Solution()
Run.createSortedArray([1,2,3,6,5,4])
([1,5,6,2])