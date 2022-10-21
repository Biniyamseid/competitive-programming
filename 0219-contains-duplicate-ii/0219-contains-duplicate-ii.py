class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        first create a window size of k 
        and slide that window, then if you found a duplicate in that window return true
        else return false
        '''
        indices = dict()
        for i,n in enumerate(nums):
            if n in indices and i-indices[n] <= k:
                return True
            indices[n] = i
        return False
    
    
        
        