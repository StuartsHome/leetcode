# Leetcode 869. Reordered Power of 2
import itertools
class Solution:
    def reorderedPowerOf2(self, N):
        for cand in itertools.permutations(str(N)):
            # The check cand[0] != '0' is a check that the candidate permutation does not have a leading zero.
            # The check bin(int("".join(cand))).count('1') == 1 is a check that cand represents a power of 2: namely,
            # that the number of ones in its binary representation is 1.
            # every power of 2 has exactly 1 bit set to 1 (the bit in that number's log base-2 index).
            if cand[0] != '0' and bin(int("".join(cand))).count('1') == 1:
                   return True
        return False
                

        """
        N = list(str(N))
        def permute(nums):
            if len(nums) < len(N):
                return[nums]

            memo = []
            for i, val in enumerate(nums):
                a = nums[:i] + nums[i+1:]
                for y in permute(a):
                    xx = [val]+y
                    xx = "".join(xx)
                    if xx.startswith("0"):
                        continue
                    else:
                        xx = int(xx)
                        #if (xx != 0) and ((xx & (xx - 1)) == 0):
                            #return True
                        memo.append(xx)
                    #xx = list(map(int, [val]+y))
                    #xx = "".join(xx)
                    #xx = str([val]+y)
                    #memo.append([val]+y)
            #return False
            return memo
        aa = permute(N)
        print(aa)
        """
Run = Solution()
Run.reorderedPowerOf2(521)
(124)