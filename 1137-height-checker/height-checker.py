class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        def generate(expect,heights):
            ans = 0
            
            for i,j in zip(expect,heights):
                if i!=j:
                    yield 1
        expect = sorted(heights)
        return sum(generate(expect,heights))
            

        