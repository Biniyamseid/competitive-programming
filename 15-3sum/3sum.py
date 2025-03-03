from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        n = len(nums)
        
        for i in range(n-2):
            if i>0 and  nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left<right:
                # if left>len(nums)-1:
                #     break
                sum = nums[i]+nums[left]+nums[right]
                if sum == 0:
                    print(i,left,right)
                    triplets.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right] == nums[right-1]:
                        right -=1
                    left+=1
                    right-=1
                elif sum <0:
                    left+=1
                else:
                    right-=1
        return triplets




# from collections import defaultdict
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:

#         triplets = []
#         nums.sort()
#         n = len(nums)
#         left = 0
#         right = len(nums)-1
#         num_to_index_max = defaultdict(list)
#         # maps numbers to their index
#         for indx,num in enumerate(nums):
#             num_to_index_max[num].append(indx)

#         for i in range(n-2):
#             if i > 0 and nums[i] == nums[i - 1]:  
#                 continue  # Skip duplicate elements for i
#             right = n-1
#             left = i+1
#             while left < right:
#                 sum = nums[i]+nums[left]+nums[right]
#                 if sum == 0:
#                     triplets.append([nums[i]+nums[left]+nums[right]])


#                     while left<right and nums[left]==nums[left]+1:
#                         left +=1
#                     while left<right and nums[right]==nums[right-1]:
#                         right-=1
#                     left+=1
#                     right -=1

                
#                 # if the sum is negative go to right
#                 if sum<0:
#                     left+=1
#                 else:
#                     right -=1
#         return triplets


            
#         sum = nums[i]
        
#         def check(left,right):
#             nonlocal triplets
#             triplet_candidate = -1* (nums[left]+nums[right]) #get the sign inverse of the result and 
#             two_pointer_set = set()
#             # two_pointer_list = [nums[]]
#             two_pointer_set.add(nums[left])
#             two_pointer_set.add(nums[right])
#             trial = sorted([nums[left],nums[right],triplet_candidate])
#             if triplet_candidate in two_pointer_set:
#                 # count = counter()
#                 if nums[left] == nums[right]:
#                     if triplet_candidate in num_to_index_max and len(num_to_index_max[triplet_candidate])>2:
#                          if trial not in triplets:
#                                 triplets.append(trial)
#                                 return True
                        

#                 else:
#                     if triplet_candidate in num_to_index_max and len(num_to_index_max[triplet_candidate])>1:
#                         if trial not in triplets:
#                             triplets.append(trial)
#                             return True
#             elif triplet_candidate not in two_pointer_set:
#                         if triplet_candidate in num_to_index_max:
#                             if trial not in triplets:
#                                 triplets.append(trial)
#                                 return True
#             return False
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 check(i,j)
#         return triplets
            


    
            

        

        
        