from sortedcontainers import SortedList

from bisect import bisect_left,bisect_right

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        """for atleast use only maximum and minimum values"""
        """for exact use step"""
        minm = float("inf")
        sets = SortedList()
        for i,val in enumerate(nums):
            if i-x>=0:
                sets.add(nums[i-x])
            if sets:
                v1 = bisect_left(sets,val)
                v2 = bisect_right(sets,val)
                # print(sets[v1],sets[v2],val,sets)
                # print(sets,v1,val)
                if v1>=len(sets):
                    v1-=1
                minm = min(minm,abs(sets[v1]-val))
                if v2>=len(sets):
                    v2-=1
                minm = min(minm,abs(sets[v2]-val))
                if v1>0:
                    v1-=1
                    minm = min(minm,abs(sets[v1]-val))

                # return minm
               
        return minm


        