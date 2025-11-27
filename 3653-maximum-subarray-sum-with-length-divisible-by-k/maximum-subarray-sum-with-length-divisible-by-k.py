class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = [inf]*k
        prefix[0]=0
        total = 0
        ans = float(-inf)
        for idx,num in enumerate(nums):
            total+=num
            leng = idx+1
            prefix_len = leng%k
            ans = max(ans,total-prefix[prefix_len])
            prefix[prefix_len] = min(prefix[prefix_len],total)
        return ans



        