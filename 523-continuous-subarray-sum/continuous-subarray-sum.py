class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # runningSum = 0
        # map = defaultdict(int)
        # map[0] = -1
        # for i in range(len(nums)):
        #     runningSum += nums[i]
        #     if (k!=0):
        #         runningSum %=k
        #     print(runningSum)
        #     prev = map[runningSum]
        #     # print(prev)
        #     # print(prev,(i-prev))
        #     if prev!=0:
        #         print("hello")
        #         if (i-prev) >1:
        #             return True
            
        #     # else:
        #     map[runningSum] = i
        # return False


            map = {0: -1}
            running_sum = 0
            
            for i, num in enumerate(nums):
                running_sum += num
                if k != 0:
                    running_sum %= k
                prev = map.get(running_sum)
                if prev is not None:
                    if i - prev > 1:
                        return True
                else:
                    map[running_sum] = i
                    
            return False


        