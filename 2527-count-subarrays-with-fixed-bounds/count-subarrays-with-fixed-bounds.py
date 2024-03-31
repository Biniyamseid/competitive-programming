class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        a = -1
        b = -1
        c = -1
        res = 0

        for i in range(len(nums)):
            cur = nums[i]
            if cur == minK:
                a = i
            if cur == maxK:
                c = i
            if cur<minK or cur >maxK:
                b = i
            if b>c:
                ans = 0
            elif a<0 or c<0:
                ans = 0
            else:
                res+= max(0,min(a,c)-b)
        return res
        