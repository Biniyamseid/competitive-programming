class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans=0
        for i in range(len(logs)):
            if logs[i]=='../':
                if ans==0:
                    continue
                ans-=1
            elif logs[i]=='./':
                continue
            else:
                ans+=1
        return ans