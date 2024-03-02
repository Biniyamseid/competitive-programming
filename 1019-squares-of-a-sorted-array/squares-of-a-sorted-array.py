class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            arr.append(num**2)
        return sorted(arr)
        