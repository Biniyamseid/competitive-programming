class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        def findDuplicate():
            visited = set()
            for num in nums:
                if num in visited:
                    return num
                visited.add(num)
        duplicate = findDuplicate()
        missing = sum(range(1,len(nums)+1)) - (sum(nums)-duplicate)
        return [duplicate,missing]
            
        