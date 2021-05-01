

def knapsack(val, weight, capacity):

    val.insert(0, 0)
    weight.insert(0,0)
    N = len(val) - 1
    def dfs(ind, total):
        if ind == 0 or total == 0:
            return 0
        if weight[ind] > total:
            return dfs(ind -1, total)
        else:
            skip = dfs(ind -1, total)
            use = weight[ind] + dfs(ind -1, total - weight[ind])
            result =  max(skip, use)
        return result
    aa = dfs(N, capacity)
    print(aa)


knapsack([1,2,3,4,5], [6,7,8,9,10], 12)