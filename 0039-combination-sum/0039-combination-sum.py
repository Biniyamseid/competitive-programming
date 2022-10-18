
class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            if i>=len(candidates) or total> target:
                return
            cur.append(candidates[i])
            print(cur)
            dfs(i,cur,total + candidates[i])
            cur.pop()
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return res
            
        