class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        nums = list(reversed(sorted(happiness)))
        ans = nums[:k]
        sum = 0
        for i,val in enumerate(ans):
            if val-i>=0:
                sum+=val-i
            else:
                sum+=0
        return sum
        