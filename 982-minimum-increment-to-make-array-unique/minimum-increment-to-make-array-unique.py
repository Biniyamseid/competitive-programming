class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        nums = [3,2,1,2,1,7]
        i = 0
        nextint = [4,5,6]
        1,1,2,2,3,7
        1-4 = 3
        i+=1
        2-5 = 3

        """
        nums.sort()
        minm = min(nums)
        nextint = []
        set1 = set(nums)
        for i in range(minm+1,len(nums)+max(nums)+1):
            if i not in set1:
                nextint.append(i)
    
        # for i in range(max(nextint)+1,max(nextint)+1+len(nums)):
        #     nextint.append(i)
        ans = 0
        i = 0
        visited = set()
        count = Counter(nums)
        for num in nums:
            if count[num]>1 and num in visited:
                while nextint[i]<=num:
                    i+=1
            if count[num]>1 and num in visited:
                
                ans += abs(nextint[i]-num)
                i+=1
            visited.add(num)
        return ans


        
        # print([i for i in range(minm+1,max(len(nums),max(nums)))])
        # for i,j in zip(nums,[i for i in range(minm+1,max(len(nums),max(nums)))]):
        #     print(i,j)
        

        