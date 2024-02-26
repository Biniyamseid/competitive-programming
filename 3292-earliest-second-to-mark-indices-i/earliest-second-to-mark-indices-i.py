class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        def binarysearch(idx):
            last = {}
            for i in range(idx):
                last[changeIndices[i]] = i
            print(last,nums)
            if len(last)!=len(nums):return  False
            cnt = 0
            
            for i in range(idx):
                if i == last[changeIndices[i]]:
                    if cnt<nums[changeIndices[i]-1]:return False
                    else: cnt-=nums[changeIndices[i]-1]
                else:
                    cnt +=1
            print("hello")
            return True
        n,m = len(nums),len(changeIndices)
        l,r = 0,m+1
        while (l<r):
            mid = (l+r)//2
            if binarysearch(mid):
                r = mid
            else:
                l=mid+1

        print(r,m+1)
        return r if r!=m+1 else -1
        