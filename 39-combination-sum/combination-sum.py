class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []
        "self,next,skip"
        def backtrack(i,array,tot = 0):
            if tot>target:
                return
            print(array)
            if len(array) >= 1 and tot == target:
                answer.append(array.copy())
                return
            for j in range(i,len(candidates)):
                array.append(candidates[j])
                backtrack(j,array,tot+candidates[j])
                array.pop()
        backtrack(0,[],0)
        return answer

            

        