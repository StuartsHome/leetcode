# Leetcode 354. Russian Doll Envelopes
import bisect
class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        nums, lis = [j for _, j in envelopes], []
        for current in nums:
            idx = bisect.bisect_left(lis, current)
            lis[idx:idx+1] = [current]
        return len(lis)
####
"""
        def liss(envs):
            def lmip(envs, tails, k):
                b, e = 0, len(tails) - 1
                while b <= e:
                    m = (b + e) >> 1
                    if envs[tails[m]][1] >= k[1]:
                        e = m - 1
                    else:
                        b = m + 1
                return b
            
            tails = []
            for i, env in enumerate(envs):
                idx = lmip(envs, tails, env)
                if idx >= len(tails):
                    tails.append(i)
                else:
                    tails[idx] = i
            return len(tails)
        
        
        def f(x, y):
            return -1 if (x[0] < y[0] or x[0] == y[0] and x[1] > y[1]) else 1
            
        envs.sort(cmp=f)
        return liss(envs)
"""
            
Run = Solution()
Run.maxEnvelopes([[15,8],[2,20],[2,14],[4,17],[8,19],[8,9],[5,7],[11,19],[8,11],[13,11],[2,13],[11,19],[8,11],[13,11],[2,13],[11,19],[16,1],[18,13],[14,17],[18,19]])


([[1,1],[1,1],[1,1]])
([[5,4],[6,4],[6,7],[2,3]])