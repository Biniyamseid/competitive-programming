class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        vis = set()
        res = []
        for i in nums:
            if i in vis:
                res.append(i)
            vis.add(i)
        return res
        