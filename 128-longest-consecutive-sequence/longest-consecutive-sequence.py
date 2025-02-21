class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        visited = set()
        ans = 0
        for num in my_set:
            if num in visited:
                continue
            # is num starting point
            if num-1 in my_set:
                continue
            cur_len = 1
            visited.add(num)
            while num+1 in my_set:
                cur_len+=1
                num+=1
            ans = max(ans,cur_len)
            
        return ans
            
            
            


            


# from typing import List

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
        
#         num_map = {}  # To store left/right boundary information
#         visited = set()
#         max_length = 0

#         for num in nums:
#             if num in visited:  # Skip duplicates
#                 continue
#             visited.add(num)

#             left = num_map.get(num - 1, 0)  # Get left sequence length
#             right = num_map.get(num + 1, 0)  # Get right sequence length
#             total_length = left + right + 1  # Total sequence length

#             num_map[num] = total_length  # Store at the current num
#             num_map[num - left] = total_length  # Update left boundary
#             num_map[num + right] = total_length  # Update right boundary
            
#             max_length = max(max_length, total_length)  # Update max length
        
#         return max_length


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         minm = min(nums)
#         # nums = [i+abs(minm)+1 for i in nums]
#         map = [[0,0] for i in range(max(nums)+2)]
#         print(map)
#         visited = set()
#         print(nums)
        
#         for i in nums:
#             if i in visited:
#                 continue
            
#             print(i)
#             map[i][0] = map[i-1][0]+1
#             map[i][1] = map[i+1][1]+1
#             if i-1 in visited:
#                 map[i-1][1] +=map[i][1]
#             if i+1 in visited:
#                 map[i+1][0]+=map[i][0]
#             visited.add(i)
#             print(i,map[i])
#         ans = 1
#         print(map)
#         for i,j in map:
#             ans = max(ans,i+j-1)
#         return ans


        