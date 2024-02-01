class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        start = nums[0]
        nums.sort()
        for i in range(2,len(nums),3):
            if nums[i]-nums[i-2]>k:
                return []
            ans.append(nums[i-2:i+1])
        return ans

        # temp = [start]
        # for i in nums[1:]:
        #     if abs(i-start) <=k:
        #         temp.append(i)
        #     else:
        #         ans.append(temp.copy())
        #         start = i
        #         temp = [start]
        # if temp:
        #     ans.append(temp.copy())
        # return ans

        











#         """
#         [1,3,4,8,7,9,3,5,1]
#         [1, 1, 3, 3, 4, 5, 7, 8, 9]


#         ideas
#         sort
#         then sliding window finding the maximum possible window of array
#         and for every number there should be at least one pair
#         that means either  with the number before or the number after it absolute difference should be <=k else return []
        
        
#         """
#         ans = []
#         nums.sort()
#         if len(nums)%3:
#             return []
#         for i in range(0,len(nums),3):
#             if abs(nums[i+2]-nums[i])>k:
#                 return []
#             ans.append(nums[i:i+3])
#         return ans
            
# #         #check if it is valid
# #         for i in range(len(nums)):
# #             if i == 0:
# #                 if abs(nums[i]-nums[i+1])>k ans nums[i]:
                    
# #             if i == len(nums)-1:
# #                 pass
# #             else:
# #                 if abs(nums[i]-nums[i-1]) > k ans abs(nums[i]-nums[i+1])>k:
# #                     return []
        
        
# #         nums.sort()
# #         print(nums)
# #         max_dif = 0
# #         for i in range(1,len(nums)):
# #             max_dif = max(max_dif,nums[i]-nums[i-1])
# #         if max_dif >k:
# #             return []
# #         return [nums[:1],nums[1:2],nums[2:]]