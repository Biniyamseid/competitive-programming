class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def findans(nums,k):
                l = 0
                ans = 0
                count = Counter()
                for i in range(len(nums)):
                    count[nums[i]]+=1
                    while len(count)>k:
                        count[nums[l]]-=1
                        if count[nums[l]] ==0:
                            del count[nums[l]]
                        l+=1
                    ans += i-l+1
                return ans

           
                
              
        return findans(nums,k)-findans(nums,k-1)
        