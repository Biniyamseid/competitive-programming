class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def helper(i,count):
            if i == len(nums):
                return 1
            res = helper(i+1,count) #skip nums[i]
            if not count[k+nums[i]] and not count[nums[i]-k]:
                count[nums[i]]+=1
                res += helper(i+1,count)
                count[nums[i]]-=1
            return res
        return helper(0,defaultdict(int))-1
        # def generate_subsets(i,subset,subsets):
        #     if i == len(nums):
        #         subsets.append(subset[:])
        #         return
        #     subset.append(nums[i])
        #     generate_subsets(i+1,subset,subsets)
        #     subset.pop()
        #     generate_subsets(i+1,subset,subsets)
        #     return subsets
        # subsets = generate_subsets(0,[],[])
        # all = len(subsets)-1

        # for subs in subsets:
        #     flag = False
        #     for i in range(len(subs)):
        #         for j in range(i+1,len(subs)):
        #             if abs(subs[i]-subs[j]) == k:
        #                 all-=1
        #                 flag = True
        #                 break
        #         if flag:
        #             break

        # return all

            
        