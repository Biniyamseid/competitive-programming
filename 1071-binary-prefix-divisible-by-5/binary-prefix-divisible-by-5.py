class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        curr = 0
        for binary in nums:
            curr = ((curr << 1)+ binary)%5
            
            if curr:
                answer.append(False)
            else:
                answer.append(True)
           
        return answer
        