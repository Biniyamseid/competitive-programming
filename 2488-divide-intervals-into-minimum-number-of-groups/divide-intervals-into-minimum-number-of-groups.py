class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for i,j in intervals:
            start.append(i)
            end.append(j)
        start.sort()
        end.sort()
        i,j = 0,0
        res = 0
        group = 0
        while i<len(start):
            if start[i]<=end[j]:
                group+=1
                i+=1
            else:
                group-=1
                j+=1
            res = max(res,group)
        return res
        