class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        prevx,prevy = points[0][0],points[0][1]
        for x,y in points[1:]:
            current_distance = max(abs(x-prevx),(abs(y-prevy)))
            answer+=current_distance
            prevx,prevy = x,y
        return answer

        