class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for i in range(len(nums))]
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]
        print(suffix)
        for i in range(1,len(nums)):
            prefix[i]=nums[i-1]*prefix[i-1]
        for i in range(len(nums)-2,-1,-1):
            print(i)
            suffix[i]= nums[i+1]*suffix[i+1]
        # suffix = suffix[::-1]
        print(prefix,suffix)
        for i in range(len(nums)):
            if i ==0:
                answer[i] = suffix[i]
            if i == len(nums)-1:
                answer[i] = prefix[i]
            else:
                answer[i] = prefix[i]*suffix[i]

        return answer


                    
        