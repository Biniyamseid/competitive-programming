class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def backtrack(sol,n):
            if len(sol)== len(set(sol)):
                ans.append(sol.copy())
            for i in range(n,len(nums)):
                sol.append(nums[i])
                backtrack(sol,i+1)
                sol.pop()

        backtrack([],0)
        return ans
        