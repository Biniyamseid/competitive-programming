class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted([i for i in range(1,n+1)],key=lambda x:str(x))
        