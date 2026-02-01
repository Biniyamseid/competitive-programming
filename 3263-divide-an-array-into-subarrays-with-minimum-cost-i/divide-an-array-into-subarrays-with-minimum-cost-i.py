class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # return first + second min + third min
        secondmin = float(inf)
        firstmin = float(inf)
        for num in nums[1:]:
            if num< firstmin:
                if firstmin<=secondmin:
                    secondmin= firstmin
                firstmin=num
            elif num<=secondmin:
                secondmin=num
        return nums[0]+firstmin+secondmin
        