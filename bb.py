# Input: abcbaaab
# output:
# bcb
# abcba
# baaab
# aaa
#  * /
 
# abcbaaab
# 0, 0

# l 0, 0, return Nothing
# l 0, 1 return Nothing
# l 1, 1 return Nothing
# l 1, 2 return Nothing
# l 2, 2 return bcb, abcba

        

# def palindromes(word):
    
#     def helper(start, l, r):
#         string = str(start)
#         while l >= 0 and r < len(word):
#             if word[l] == word[r]:
#                 if l != r:
#                     string = word[l] + string + word[r]
#                 l -= 1 
#                 r += 1
                
#             if string not in self.result and len(string) >= 3:
#                 self.result.append(string)
    
#     self.result = []
#     for char in range(len(word)):
#         self.result.append(helper(word[char], char, char))
#         self.result.append(helper(word[char], char, char + 1))
#     return self.result


# #
