def combinationsum(candidates,tar):
    res = []

    def dfs(i,cur,total):
        if total == tar:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > tar:
            return

        cur.append(candidates[i])
        dfs(i,cur,total+candidates[i])
        cur.pop()
        dfs(i+1,cur,total)
    dfs(0,[],0)
    return res
print(combinationsum([2,3,6,7],7))
