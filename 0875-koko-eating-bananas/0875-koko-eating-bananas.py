class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        l = 1
        r = max(piles)
        res = max(piles)
        while l<= r:
            mid = (l+((r-l)//2))
            time = 0
            for i in range(len(piles)):
                time += int(math.ceil(piles[i]/mid))
            if time >h:
                l = mid+1
            elif time<=h:
                res = min(res,mid)
                r = mid -1        
        return res
                
        
            
            
                
                
                
                
        