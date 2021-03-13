
# Leetcode 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1, nums2):
        min_words = min((nums1), (nums2))
        max_words = max((nums1), (nums2))
        """
        result = set()

        for i in nums1:
            if i in nums2:
                result.add(i)
        print(result)
"""

        set1 = set(nums1)
        set2 = set(nums2)
        print(list(set1 & set2))
        



Run = Solution()
Run.intersection([4,9,5], [9,4,9,8,4])
        
        