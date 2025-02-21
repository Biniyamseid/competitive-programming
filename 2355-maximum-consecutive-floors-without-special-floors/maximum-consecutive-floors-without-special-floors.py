class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.append(bottom -1)
        special.append(top +1)
        special.sort()
        ans = 0
        for i in range(1,len(special)):
            ans = max(ans,special[i]-special[i-1]-1)
        return ans



        