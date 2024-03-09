class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2 = set(nums2)
        for i in nums1:
            if i in nums2:
                return i
        return -1
        