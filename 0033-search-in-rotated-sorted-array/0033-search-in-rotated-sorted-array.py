class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l+((r-l)//2)
            if target == nums[mid]:
                return mid
            #left sorted array
            if nums[l] <= nums[mid]:
                #should I go to the right
                #or is it going to be out of my range(is it rotated from left) 
                #always think this is your left most boundary
                if target > nums[mid] or target < nums[l]: 
                    l = mid+1
                else:
                    r = mid-1
                
                
            
            
            
            #right sorted array
            else:
                #should I go to the right
                #or is it going to be out of my range(is it rotated from my left)  #always think this is your right most boundary
                #every time you have two choices either move to the right or move to the left
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid + 1
            #steps:
             #detect whether we are on the right sorted array or the left sorted arrray
                    #if nums[left] <= nums[middle] it is on hte left sorted array
            #remember every time you have to choices either move to the right or move to the left
            #at this the additional code on the original binary search program is "is it out of my boundary?" :
                    #in the left sorted array case: 
                            #is it smaller than my smaller value?
                                    #if so go to the right
                    #in the right sorted case:
                            #is it greater than my greater value?
                                    #if so go to the left
        return -1
                
        