class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        counter = Counter(nums1)
        counter2 = Counter(nums2)
        answer = []

        for i in set1:
            if i in set2:
                times = min(counter[i],counter2[i])
                answer.extend([i]*times)
        return answer
        