class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        def is_possible(num1):
            saved_sum = sum(num1)
            save = num1.copy()
            m = max(save)
            save.remove(m)
            res = sum(save)
            if res <=m:
                return 0
            else:
                return saved_sum
        def calculator(nums):
            nums.sort()
            i = 0
            j = len(nums) -3
            for h in range(j,-1,-1):
                temp = nums[h:h+3]
                possible = is_possible(temp)
                if possible:
                    return possible
            return 0
        return calculator(nums)
