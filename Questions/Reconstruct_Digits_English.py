# Leetcode 423. Reconstruct Original Digits From English
from itertools import chain
from collections import Counter
class Solution:
    def originalDigits(self, s):
        # 1. 
        cnt = Counter(s)
        ans = {}
        
        ans[0] = cnt['z']
        ans[2] = cnt['w']
        ans[4] = cnt['u']
        ans[6] = cnt['x']
        ans[8] = cnt['g']
        
        ans[3] = cnt['h'] - ans[8]
        ans[5] = cnt['f'] - ans[4]
        ans[7] = cnt['v'] - ans[5]
        ans[9] = cnt['i'] - ans[6] - ans[5] - ans[8]
        
        ans[1] = cnt['o'] - ans[0] - ans[2] - ans[4]
        
        output = ""
        for i in range(10):
            output += str(i) * ans[i]
            
        return output

        # 2.
        # Difficult solution to understand that follows the same process as first solution
        """
        c = Counter(s)
        d = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
        
        res = [''] * 10
        for i in chain(range(0,10,2), range(1,10,2)):
            cur = Counter(d[i])
            if not cur - c:
                k = min(c[x] for x in cur)
                res[i] = str(i) * k
                for x in cur: c[x] -= k                  

        return ''.join(res)
        """

Run = Solution()
Run.originalDigits("zeroonetwothreefourfivesixseveneightnine")
("fviefuro")
("zerozero")
("owoztneoer")


