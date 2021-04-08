# Leetcode 447. Number of Boomerangs.

class Solution:
    def numberOfBoomerangs(self, points):
        result = 0
        memo = []
        for i in points:
            current = i
            total = 0
            for x in points:
                if x != current:
                    diff = [current[0] - x[0], current[1] - x[1]]
                    memo.append(diff)
                    #if (x[0] <= current[0] + 2 and x[0] >= current[0] - 1 and x[1] <= current[1] + 2 and x[1] >= current[1] - 1):
                        #total += 1
            # if total >= 2:
            #     result += 1
        print(memo)

Run = Solution()
Run.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])
# Expected 5
([[0,0],[1,0],[2,0]])