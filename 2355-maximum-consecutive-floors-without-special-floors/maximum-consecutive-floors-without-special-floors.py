class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        starting = bottom
        left = special[0]- starting
        right = top-special[-1] 
        ans = max(right,left)
        for i in range(1,len(special)):
            ans = max(ans,special[i]-special[i-1]-1)
        return ans



        