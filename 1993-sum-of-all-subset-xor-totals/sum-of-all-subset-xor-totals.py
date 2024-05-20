class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def generate_subsets(nums,idx,subset,subsets):
            if idx == len(nums):
                subsets.append(subset[:])
                return
            subset.append(nums[idx])
            generate_subsets(nums,idx+1,subset,subsets)
            subset.pop()
            generate_subsets(nums,idx+1,subset,subsets)
        subsets = []
        generate_subsets(nums,0,[],subsets)
        result = 0
        for subset in subsets:
            subset_xor_total = 0
            for num in subset:
                subset_xor_total ^= num
            result += subset_xor_total
        return result
        