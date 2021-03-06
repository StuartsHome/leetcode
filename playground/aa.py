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



# class Solution:
#     def wordSubsets(self, A, B):
#         # Construct unique subset for B
#         s = set(A)
#         required = {}
#         for i in B:
#             for j in i:
#                 count = i.count(j)
#                 if j not in required or count > required[j]:
#                 # Instead of If statement can use the below
#                 # max(i.count(j), required.get(char, 0))
#                     required[j] = count
#         # print(required)
#         for i in A:
#             for j in required:
#                 if i.count(j) < required[j]:
#                     s.remove(i)
#                     break
#         return list(s)


# Run = Solution()
# Run.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"])





class Solution:
    def maxScore(self, cardPoints, k):
        
        N = len(cardPoints) - k
        minSubArraySum = float('inf')
        j = curr = 0

        for ind, val in enumerate(cardPoints):
            curr += val
            if ind - j + 1 > N:
                curr -= cardPoints[j]
                j += 1
            if ind - j + 1 == N:
                minSubArraySum = min(minSubArraySum, curr)
        return sum(cardPoints) - minSubArraySum

Run = Solution()
Run.maxScore([1,2,3,4,5,6,1], 3)