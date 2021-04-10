
# def combinations(l, n):
#     solutions = []
#     if len(l) == 0:
#         return []
#     if n == 1:
#         solutions = [[element] for element in l]
#         return solutions

#     for index in range(len(l) - 1):
#         sub_solutions = combinations(l[index + 1:], n -1)
#         solutions.append([l[index]] + sub_solutions)
#     return solutions
# aa = combinations([1,2,3,4], 3)
# print(aa) 

def perm(a, n, k=0):
   if k == n:
      print(a)
   else:
      for i in range(k, len(a)):
         a[k], a[i] = a[i] ,a[k]
         perm(a, n, k+1)
         a[k], a[i] = a[i], a[k]

perm([1,2,3,4], 4)