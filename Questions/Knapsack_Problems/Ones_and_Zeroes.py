# Leetcode ?. Ones and Zeroes

class Solution:
    def findMaxForm(self, strs, m, n):
        def findMax(strs, i, m, n):
            counter = 0
            if i <= len(strs)-1:                
                if m > 0 or n > 0:
                    # use it or skip it
                    m1 = strs[i].count('0')
                    n1 = strs[i].count('1')
                    use = 0
                    
                    # skip it
                    skip = findMax(strs, i+1, m, n)
                    
                    # use it
                    if m1 <= m and n1 <= n:
                        use = findMax(strs, i+1, m-m1, n-n1) + 1
                    
                    # update counter
                    counter = max(use, skip)
                                
            return counter
            
        counter = findMax(strs, 0, m, n)
        return counter
        

Run = Solution()
Run.findMaxForm(["10","0001","111001","1","0"], 5, 3)
(["10","0","1"], 1, 1)

"""
def findMaxForm(self, strs, m, n):
    self.memo = {}
    def findMax(strs, i, m, n):
        if i <= len(strs)-1:
            if (i, m, n) in self.memo:
                return self.memo[(i,m,n)]
            
            if m > 0 or n > 0:
                # use it or skip it
                m1 = strs[i].count('0')
                n1 = strs[i].count('1')
                use = 0
                
                # skip it
                skip = findMax(strs, i+1, m, n)
                
                # use it
                if m1 <= m and n1 <= n:
                    use = findMax(strs, i+1, m-m1, n-n1) + 1
                
                # update counter
                counter = max(use, skip)
                self.memo[(i,m,n)] = counter
                
                return self.memo[(i,m,n)]
        
        return 0
        
    counter = findMax(strs, 0, m, n)
    return counter
"""