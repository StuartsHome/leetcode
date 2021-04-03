def solution(S):
    memo = {}
    total = 0
    for i in range(len(S) - 1):
        ss = S[i] + S[i + 1]
        if ss not in memo:
            memo[ss] = [i]
        else:
            ind = i - memo[ss][0]
            #memo[ss].append()
            memo[ss].append(ind)
    
    # for key, value in enumerate(memo.values()):
    #     print(key, value, memo[key])
    for x in memo:
        #total = memo[x]
        if len(memo[x]) > 1:
            total = max(total, memo[x][-1])
    print(total)
    

        



solution("aakmaakmakda")



# def longestDiverseString(a, b, c):
#         memo = {'a':a, 'b':b, 'c':c}
#         filler = ['x', 'x']
#         while sum(memo.values()) > 0:
#             sub_string = ''
#             for x in memo.keys():
#                 if memo[x] > 0 and not (filler[-1] == x and filler[-2] == x):
#                     if not sub_string:
#                         sub_string = x
#                     elif memo[x] > memo[sub_string]:
#                         sub_string = x
#             if not sub_string:
#                 break
#             filler += [sub_string]
#             memo[sub_string] -= 1
            
#         return ''.join(filler[2:])

# longestDiverseString(6,1,1)
# (1,3,1)
# (0,1,8)

# # umm

# def solution(A):
#     # write your code in Python 3.6
#     memo = {}
#     for i in A:
#         if i in memo:
#             memo[i] -= 1
#         else:
#             memo[i] = 1
#     print(memo.values())


# solution([1,2,2,1])

# [7,7,7]
# [1,2,2,3]
# [10,1,1,10,2]