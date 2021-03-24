# Leetcode 870. Advantage Shuffle

class Solution:
    def advantageCount(self, A, B):
        copy_A = sorted(A)
        copy_B = sorted(B)

        assigned = {b: [] for b in B}
        remaining = []

        j = 0
        for a in copy_A:
            if a > copy_B[j]:
                assigned[copy_B[j]].append(a)
                j += 1
            else:
                remaining.append(a)
        
        return [assigned[b].pop() if assigned[b] else remaining.pop() for b in B]







Run = Solution()
Run.advantageCount([12,24,8,32], [13,25,32,11])

([2,7,11,15], [1,10,4,11])