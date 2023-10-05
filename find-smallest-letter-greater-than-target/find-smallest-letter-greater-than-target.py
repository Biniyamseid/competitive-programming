class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        n = len(letters)
        ans = []
        right = n-1
        while left<=right:
            mid = (left+right)//2
            if letters[mid]>target:
                ans.append(letters[mid])
                right = mid-1
            if letters[mid]<=target:
                left = mid+1
        return ans[-1] if ans else letters[0]
        