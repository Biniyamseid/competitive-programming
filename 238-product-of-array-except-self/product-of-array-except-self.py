class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        result = [0]*n
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n-1,-1,-1):
            result[i]*=postfix_product
            postfix_product *= nums[i]
        return result





        # left = 1
        # right = 1
        # leftarr=[]
        # rightarr = nums.copy()
        # res = []
        # for i in nums:
        #     leftarr.append(left)
        #     left*=i
        # leftarr.extend([1,1,1])
        # for i in range(len(nums)-1,-1,-1):
        #     rightarr[i]=right
        #     right*=nums[i]
        # rightarr.append(1)
        # rightarr.extend([1,1,1,1])
        # print(leftarr,rightarr)
        # for i in range(len(nums)):
        #     if i+1<len(rightarr) and i<len(leftarr):
        #         res.append(leftarr[i]*rightarr[i+1])
        # return res
        

