class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxm = 0

        while l <= r:
            # if l>len(hei)
            curr = min(height[l],height[r])*(r-l)
            print(curr)
            maxm = max (maxm,curr)
            print(maxm)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxm

        