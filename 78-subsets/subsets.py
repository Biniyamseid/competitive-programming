class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generate_subsets(index,nums,subset,subsets):
            if index == len(nums):
                subsets.append(subset[:])
                return
            subset.append(nums[index])
            generate_subsets(index+1,nums,subset,subsets)
            subset.pop()
            generate_subsets(index+1,nums,subset,subsets)
            return subsets
        return generate_subsets(0,nums,[],[])

            
        