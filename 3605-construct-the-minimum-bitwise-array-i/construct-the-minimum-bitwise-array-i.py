class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
       ans = []
       for num in nums:
        answer = False
        for candidate in range(1,num):
            if candidate | (candidate+1)  == num:
                ans.append(candidate)
                answer = True
                break
        if not answer:
            ans.append(-1)
       return ans
        
        

            