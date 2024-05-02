class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set()
        k = sorted(nums)
        ans = -1
        for num in k:
            if num<0:
                s.add(num)
            else:
                if -1*num in s:
                    ans = num
        return ans
        