

class Solution:
    def aa(self, arr, k, x):

        left, right = 0, len(arr)-1
        while left < right:
            ind = left + (right - left) // 2
            val = arr[ind]
            if val >= x:
                right = ind
            else:
                left = ind + 1
        right = left
        left -= 1

        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue
            if right == len(arr) or (abs(x) - abs(arr[left] < abs(x) - abs(arr[right]))):
                left -= 1
            else:
                right += 1
        bb = arr[left + 1:right]
        print(bb)
        

Run = Solution()
Run.aa([1,2,3,4,5],4, 3)
([0,0,1,2,3,3,4,7,7,8], 3, 5)