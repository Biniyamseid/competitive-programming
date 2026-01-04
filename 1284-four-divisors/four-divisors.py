import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            count, divisors = 0,[]
            for j in range(1,math.ceil(math.sqrt(nums[i]))):
                # print(nums[i],j)
                if nums[i]%j == 0:
                    divisors.append(j)
                    divisors.append(nums[i]//j)
                    count +=2
                # print(divisors)
                if count >4:
                    count = 0
                    divisors = []
                    break
            if nums[i]%math.sqrt(nums[i])==0:
                count +=1
                divisors.append(math.sqrt(nums[i]))

            if count ==4:
                print(answer,count,divisors)
                answer+=sum(divisors)
        
        return answer
            
                
