class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        prev_one = False
        distance=0
        for i in range(len(nums)):
            if nums[i]==0:
                distance+=1
            else:
                if prev_one and (distance <k):
                    return False
                prev_one = True
                distance = 0
        return True
        # print(zeros)
        # for split in zeros:
        #     if len(split)<k:
        #         return False
        # return True
        