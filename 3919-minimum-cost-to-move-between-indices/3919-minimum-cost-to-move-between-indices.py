class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        answer,n= [],len(nums)
        # find closest index
        closest_indices = [0]*len(nums)
        closest_indices[0]=1
        closest_indices[len(nums)-1]=len(nums)-2
        # since it is strictly increasing  the adjacent is the neighbout
        for i in range(1,len(nums)-1):
            if abs(nums[i]-nums[i-1])<=abs(nums[i]-nums[i+1]):
                closest_indices[i] = i-1
            else:
                closest_indices[i]=i+1

        prefix = [0]*n
        postfix=[0]*n
        total_psum = 0
        print(closest_indices)
        for i in range(n-1):
            if closest_indices[i]==i+1:
                total_psum+=1
            else:
                total_psum+=abs(nums[i]-nums[i+1])
            prefix[i+1]=total_psum
        total_postsum = 0
        for i in range(n-1,0,-1):
            if closest_indices[i]==i-1:
                print(1)
                total_postsum+=1
            else:
                total_postsum+=abs(nums[i]-nums[i-1])
                print(abs(nums[i]-nums[i-1]))
            postfix[i-1]= total_postsum
        for i,j in queries:
            if i<j:
                answer.append(prefix[j]-prefix[i])
            else:
                answer.append(postfix[j]-postfix[i])
        return answer

            
            
                
  
        