class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # make custom range with two offset , full and partial offset,2 and 1 intersection
        # sort by end
        intervals = sorted(intervals,key = lambda x:(x[1],-x[0]))
        answer = set()
        # intervals = intervals[::-1]
        
        x,y = float(inf),float(inf)
        for i,j in intervals:
            if x==float(inf) and y==float(inf):
                x,y = j-1,j
                answer.add(x)
                answer.add(y)
            elif y<i:
                x,y = j-1,j
                answer.add(x)
                answer.add(y)
            elif  x<i:
                x=y
                y=j
                answer.add(y)
           

        return len(answer)

        # for i,j in intervals:
        # nums = set()
        # for i,j in intervals:
        #     if i not in nums:
        #         nums.add(i)
        #     if j not in nums:
        #         nums.add(j)
        # return len(nums)
        