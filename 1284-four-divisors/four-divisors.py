import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            count, divisors = 0,[]
            r = math.sqrt(nums[i])
            for j in range(1,math.ceil(r)):
                if nums[i]%j == 0:
                    divisors.append(j)
                    divisors.append(nums[i]//j)
                    count +=2
                if count >4:
                    count = 0
                    divisors = []
                    break
            if nums[i]%r==0:
                count +=1
                divisors.append(r)

            if count ==4:
                answer+=sum(divisors)
        
        return answer
            
                
