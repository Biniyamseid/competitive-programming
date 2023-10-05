class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        n = len(nums)
        right = n-1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        # Post-processing:
        # End Condition: left == right
        if nums[left] == target:
            return left
        return -1