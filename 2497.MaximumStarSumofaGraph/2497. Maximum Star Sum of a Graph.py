class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        from collections import defaultdict
        defdic = defaultdict(list)

        for i, j in edges:
            if vals[j] > 0:
                defdic[i].append(vals[j])
            if vals[i] > 0:
                defdic[j].append(vals[i])
        for i in defdic:
            if defdic[i]:
                defdic[i] = sorted(defdic[i], reverse=True)
        res = max(vals)
        for i in defdic:
            if defdic[i]:
                # if vals[i]>0:
                res = max(sum(defdic[i][:k])+vals[i], res)
                # else:
                #res = max(sum(defdic[i][:k]),res)
        return res
