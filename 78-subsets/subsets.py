class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        def backtrack(array,n):
            answer.append(array.copy())
            for i in range(n,len(nums)):
                array.append(nums[i])
                backtrack(array,i+1)
                array.pop()
        backtrack([],0)
        return answer

        