class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        vis = set()
        not_ans = set()
        for i in nums:
            if i in vis:
                not_ans.add(i)
            vis.add(i)
        for i in nums:
            if i not in not_ans:
                ans.append(i)
        return ans
            
        