# from itertools import product
# class WordFilter:
#     def __init__(self, words):
#         self.d = {}
#         # def prod(*args, repeat=2):
#         #     pools = [tuple(pool) for pool in args] * repeat
#         #     result = [[]]
#         #     for pool in pools:
#         #         result = [+[y] for x in result for y in pool]
#         #     for prod in result:
#         #         yield tuple(prod)
                
#         for i, word in enumerate(words):
#             for p, s in product(range(len(word) + 1), repeat=2):
#                 self.d[word[:p], word[s:]] = i
#         print(self.d)
#     def f(self, prefix, suffix):
#         return self.d.get((prefix, suffix), -1)

# Run = WordFilter(["cabaabaaaa","ccbcababac"])
# # Run.f("a","aa")
# # ( ["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"])



# class Solution:
#     def LIS(self, nums):

#         for i in range(1, len(nums)):
#             for j in range(i):
#                 print(i, j)


# Run = Solution()
# Run.LIS([0,1,0,3,2,3])
# ([4,10,4,3,8,9])
# ([-2, -1])
# ([10,9,2,5,3,7,101,18])






