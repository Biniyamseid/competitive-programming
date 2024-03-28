class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        c = defaultdict(int)
        for i in range(len(nums)):
            curr = nums[i]
            c[curr]+=1
            while curr in c and c[curr] > k:
                c[nums[l]]-=1
                l+=1

                if c[curr]==0:
                    del c[curr]
            # if c[curr] == 0:
            #     del c[curr]
            ans = max(i-l+1,ans)
        return ans
            



        