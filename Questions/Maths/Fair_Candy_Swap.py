# Leetcode 888. Fair Candy Swap
# The goal is to have both lists to have the same sum after trading one item with each other.
# The value of the sum therefore has to be equal to the average of the two lists i.e [sum(listA) + sum(listB)] / 2

# The average of both sums will be the total amount that both of them will have at the end.
# This means if we have to add some value diff to A, the same value diff will be subtracted
# from B and vice versa.

# For every candy i Alice has, if Bob has difference + i
class Solution:
    def fairCandySwap(self, A, B):
        sum_A = sum(A)
        sum_B = sum(B)
        diff = (sum(A) - sum(B)) // 2   # divide by 2 for the average difference between A and B
        
        set_A = set(A)                  # for constant time, could also use hash set
        for i in B:                     # for every candy Bob has
            if diff + i in set_A:       # if Alice has the diff plus i
                #return [diff + i, i]
                print((diff + i), i)

        """     Alternative, using setB instead of setA
        set_B = set(B)
        for x in A:
            if x + diff in set_B:
                return [x, x + diff]
        """
    
Run = Solution()
Run.fairCandySwap([1,2,5], [2,4])


([2], [1,3])