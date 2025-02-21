class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3:
            return []
        return [int(num/3-1),int(num/3),int(num/3+1)]
        