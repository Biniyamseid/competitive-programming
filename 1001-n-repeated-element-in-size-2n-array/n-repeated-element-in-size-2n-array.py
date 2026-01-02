class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = Counter(nums)
        counte = {}
        for i in count:
            counte[count[i]]=i
        return counte[max(counte)]
       

        