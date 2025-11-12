class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ones = nums.count(1)
        if ones>=1:
            return len(nums)-ones
        min_len = float("inf")
        for i in range(len(nums)):
            g = nums[i]
            for j in range(i+1,len(nums)):
                g = gcd(g,nums[j])
                if g == 1:
                    min_len = min(min_len,j-i+1)
                    break
        if min_len == float("inf"):
            return -1
        return min_len-1 + len(nums)-1

        