class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        answer, parity= [],[]
        even,odd,n = 0,0,len(nums)
        for i in range(n-1,-1,-1):
            if nums[i]%2:
                odd+=1
            else:
                even+=1
            parity.append((even,odd))
        for i in range(n):
            even_count,odd_count = parity.pop()
            if nums[i]%2==0:
                answer.append(odd_count)
            else:
                answer.append(even_count)
        return answer
            
  
                
            
            
      
            
        