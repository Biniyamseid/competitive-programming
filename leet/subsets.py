from cgitb import reset


def subsets(nums):
    res = []
    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
        else:
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
    dfs(0)
    return res
print(subsets([1,2,3]))


def dfs(i):
    if i >= len(nums):
        res.append(subset.copy())
    else:
        subset.append(nums[i])
        dfs(i+1)
        subset.pop()
        dfs(i+1)
    return res
