class Solution:
    def removeDuplicates(self, numbers: List[int]) -> int:
        f,s = 1,1
        for l in range(1,len(numbers)):
            if numbers[l-1] != numbers[l]:
                numbers[f] = numbers[l]
                f +=1
        return f
        