# Leetcode ?. The K Weakest Rows in a Matrix

class Solution:
    def kWeakestRows(self, mat, k):
        memo = {}
        result = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    if i in memo:
                    #print("row:", i,"col:",j)
                        memo[i] += 1
                    else:
                        memo[i] = 1
                elif mat[i][j] == 0 and i not in memo:
                    memo[i] = 0
                else:
                    continue
        
        for i in range(k):
            key_to_delete = min(memo, key=lambda k: memo[k])
            # alternative "del d[max(d, key=d.get)]"
            result.append(key_to_delete)
            del memo[key_to_delete]
        print(result)
mat = [
[1,0],
[0,0],
[1,0]]


Run = Solution()
Run.kWeakestRows(mat, 2)

[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

"""
for i in range(len(mat)):
    counter = 0
    for j in range(len(mat[i])):
        counter += 1
        if mat[i][j] == 1:
            result.append((i, counter))
        else:
            break

for i in result:
    row, col = i
    print(row)
"""