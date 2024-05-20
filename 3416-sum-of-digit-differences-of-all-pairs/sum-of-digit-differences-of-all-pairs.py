class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        """[13,23,12]"""
        count = 0
        
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         cur = str(nums[j])
        #         prev = str(nums[i])
        #         for l,n in zip(cur,prev):
        #             if l!=n:
        #                 count +=1
        # return count
        ans = 0
        counter = [[0]*10 for i in range(11)]
        wide = len(nums)
        # print(counter)
        # 
        # 
    
        for n in nums:
            print(n)
            for i in range(0,len(str(nums[0]))):
                print(n)
                if not n:
                    break
                
                counter[i][n%10]+=1
                
                n = n//10

        for i in range(len(counter)):
            for j in range(len(counter[0])):
                ans += counter[i][j]*(wide-counter[i][j])
            
        return ans//2
        
   
                    
                
        
        