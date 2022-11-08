class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total = 0
        stack = []
        nums.sort()
        for num in nums:
            if stack and stack[-1] == num:
                stack.pop()
            else:
                stack.append(num)
        return stack
    
        
        
        
            
        