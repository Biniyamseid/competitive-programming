class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        # case: number itself and half of it appeared before
        # first_appearance , last appearance
        # 4,8,4,8
        # {}
        dp = [0]*(len(nums)+1)
        n = len(nums)
        if len(nums)>=3:
            dp[3]=1
            for i in range(4,n+1):
                dp[i] = dp[i-1]+(((i-1)*(i-2))//2)
    


        zero_count = 0
       
        counter = defaultdict(int)
        visited= set()
        double_counter = defaultdict(int)
        index_tracker = defaultdict(list)
        answer = 0
        for num in nums:
            if not index_tracker[num]:
                index_tracker[num].extend([-1,-1])
        for i,num in enumerate(nums):
            
            if num*2 in visited:
                
                    double_counter[num]+=counter[num*2]

            if num in visited and num/2 in visited:
                if index_tracker[num][0]<index_tracker[num/2][1]:
                    if num/2!=0:
                        answer+=double_counter[num/2]
                    else:
                         zero_count+=1
            if num not in visited:
                index_tracker[num][0]=i
                visited.add(num)
            index_tracker[num][1]=i
            counter[num]+=1
        if counter[0]>=3:
            answer+=dp[counter[0]]
        return answer%(10**9+7)
            

        