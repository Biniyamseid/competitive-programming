class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        # l = 0
        # psum=0
        # ans = 0
        # for i in range(len(nums)):

        #     psum += nums[i]
        #     if psum == goal:
        #         print(l,i,psum,goal)
        #         ans +=1
        #     flag = False
        #     while (psum>goal or (flag and psum>=goal)) and l<i:
        #         flag = True
        #         psum-=nums[l]
        #         l+=1
        #         if psum==goal:
        #             print(l,i,psum,goal)
        #             ans+=1
        # return ans
        totalcount = 0
        d = defaultdict(int)
        d[0] = 1
        # d = collections.Counter({0:1})
        pr = 0
        for i in range(len(nums)):
            pr+=nums[i]
            
            totalcount+=d[pr-goal]
            d[pr]+=1
        print(d)
        return totalcount



        # ans = 0
        # for i in range(len(nums)):
        #     total = 0
        #     if total == goal:
        #             ans +=1
        #     for j in range(i,len(nums)):
        #         total+=nums[j]
        #         if total == goal:
        #             ans+=1
        #     return total


