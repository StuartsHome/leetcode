# Leetcode ?. 
class Solution:
    def reorderedPowerOf2(self, N):
        N = list(str(N))
        def permute(nums):
            if len(nums) < 3:
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
        # result = 
        # for i in aa:


Run = Solution()
Run.reorderedPowerOf2(521)
(124)