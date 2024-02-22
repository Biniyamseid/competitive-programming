class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        trust = defaultdict(list)
        rtrust = defaultdict(list)
        for i,j  in t:
            trust[i].append(j)
            rtrust[j].append(i)
        ans = []
        for i in range(1,n+1):
            if not trust[i] and len(rtrust[i])==n-1:
                ans.append(i)
        if len(ans)==1:
            return ans[0]
        return -1
        