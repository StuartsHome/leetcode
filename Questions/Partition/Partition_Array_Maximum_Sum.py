class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        if len(arr) == 1 and k == 1:
            return arr
        N = len(arr)
        if N % k != 0:
            total = N // k
        total = N / k
        temp = []
        counter = 0
        total_2 = 0
        for i in range(len(arr)):
            temp.append(arr[i])
            counter += 1
            if counter == k:
                total_2 += max(temp) * len(temp)
                counter = 0
                temp = []
        return total_2
Run = Solution()
Run.maxSumAfterPartitioning([1,15,7,9,2,5,10],3)