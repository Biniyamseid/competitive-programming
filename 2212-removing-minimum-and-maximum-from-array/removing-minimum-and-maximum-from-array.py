class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # get index of max = 1, get index of min min = 5 total n = 8
        # 8-1-(8-5-1) = 5
        # min(5+1,8-1) == min(greaterindex+1,lessindex-1)
        minm,maxm  = min(nums),max(nums)
        n = len(nums)
        min_idx,max_idx =0,0
        for i,val in enumerate(nums):
            if val == minm: min_idx = i
            if val==maxm: max_idx = i
        mn,mx = min(min_idx,max_idx),max(max_idx,min_idx)
        print(n,mn,mx)
        # a = n-mn-(n-mx-1)
        a = mn+(n-mx)+1
        b = mx+1
        c = n-mn
        print(a,b,c)
        
        answer = min(a,b,c)
        return answer


        