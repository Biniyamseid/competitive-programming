class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        curr = ""
        for binary in nums:
            curr+=str(binary)
            if int(curr,2)%5:
                answer.append(False)
            else:
                answer.append(True)
           
        return answer
        