class Solution:
    def removeDuplicates(self, numbers: List[int]) -> int:
        if not numbers:
            return 0
        slow = 0
        for fast in range(1,len(numbers)):
            if numbers[fast] != numbers[slow]:
                slow+=1
                numbers[slow] = numbers[fast]
        return slow+1
            
        