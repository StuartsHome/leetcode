# Leetcode ?. Binary Trees With Factors


class Solution:
    def numFactoredBinaryTrees(self, arr):
        s_arr, N = set(arr), 10**9 + 7
        
        def dp(num):
            ans = 1
            for cand in s_arr:
                if num % cand == 0 and num//cand in s_arr:
                    ans += dp(cand)*dp(num//cand)
            return ans
        
        return sum(dp(num) for num in s_arr) % N
Run = Solution()
Run.numFactoredBinaryTrees([18,3,6,2])

([2,4,5,10])

([2,4])


####### 1.
class Solution():
    def numFactoredBinaryTrees(self, A):
        A.sort()
        N = len(A)
        dp = {A[0]: 1}
        for i in range(1, N):
            dp[A[i]] = 1
            for j in range(i):
                div, mod = divmod(A[i], A[j])
                if div < A[j]: break
                if mod != 0: continue
                if div in dp: 
                    mul = dp[div] * dp[A[j]]
                    dp[A[i]] += mul if div == A[j] else 2 * mul
                    
        return sum(dp.values()) % (10 ** 9 + 7)

# 2.
class Solution():
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        dic = {num:1 for num in A}
        for i in xrange(1,len(A)):
            for j in xrange(i):
                q,res = divmod(A[i],A[j])
                if res == 0 and q in dic:
                    dic[A[i]] += dic[q] * dic[A[j]]
        return sum(dic.values()) % (10 **9 + 7)

