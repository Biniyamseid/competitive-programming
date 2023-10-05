class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        for i in nums1:
            for j in nums2:
                if i==j:
                    res.add(i)
        return list(res)
        

            
        