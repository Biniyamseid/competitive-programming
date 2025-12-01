class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l = 1
        r = sum(batteries)//n
        
        def good(time):
            total = 0
            for b in batteries:
                total += min(b,time)
            return total >= n*time
            


        while l<=r:
            mid = (l+r)//2
            if good(mid):
                l = mid+1
            else:
                r = mid-1
        return l-1
       


# class Solution:
#     def maxRunTime(self, n: int, batteries: List[int]) -> int:
#         batteries = sorted(batteries,reverse=True)
#         if len(batteries)==n:
#             return min(batteries)
#         topn = batteries[:n]
#         remaining = batteries[n:]
#         level = min(topn) #3
#         top_remainder = 0
#         for i in topn:
#             if i>level:
#                 top_remainder+= (i-level)
#         remainder = sum(remaining)
#         return ((level + (remainder+top_remainder))//n)


# class Solution:
#     def maxRunTime(self, n: int, batteries: List[int]) -> int:
#         batteries = sorted(batteries,reverse=True)
#         ans = 0


#         def calc(battery,total):
#             battery = sorted(battery,reverse=True)
#             nonlocal ans
#             if not battery:
#                 return total
#             topn = battery[:n]
#             remaining = battery[n:]
#             level = min(topn) #3
#             top_remainder = 0
#             next_round = []
#             for i in topn:
#                 if i>level:
#                     top_remainder+= (i-level)
#                     next_round.append(i-level)
#             # print(level,"level")
#             if len(battery)>=n:
#                 ans+=level
#             elif len(battery)==1:
#                 ans += (level)//n
#             elif len(battery)<n:
#                 ans += sum(battery)//n
#             if not remaining:
#                 return total
#             next_round.extend(remaining)
#             remainder = sum(remaining)
            
#             return calc(next_round,total+level)
        
#         soln =  calc(batteries,0)
#         return ans

#         if len(batteries)==n:
#             return min(batteries)
        
#         topn = batteries[:n]
#         remaining = batteries[n:]
#         level = min(topn) #3
#         top_remainder = 0
#         for i in topn:
#             if i>level:
#                 top_remainder+= (i-level)
#         remainder = sum(remaining)

#         return level + (remainder+top_remainder)//n
            


