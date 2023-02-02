class Solution:
    def minimumOperations(self, A: List[int]) -> int:
        return len(set(A) - {0})
