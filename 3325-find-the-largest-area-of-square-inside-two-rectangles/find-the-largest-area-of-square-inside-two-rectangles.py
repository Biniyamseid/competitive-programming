class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        n = len(bottomLeft)
        max_area = 0

        for i in range(n):
            for j in range(i + 1, n):
                # Intersection rectangle
                left = max(bottomLeft[i][0], bottomLeft[j][0])
                right = min(topRight[i][0], topRight[j][0])
                bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                top = min(topRight[i][1], topRight[j][1])

                if left < right and bottom < top:
                    width = right - left
                    height = top - bottom
                    side = min(width, height)
                    max_area = max(max_area, side * side)

        return max_area

# class Solution:
#     def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
#         maxarea = 0
#         for i in range(len(bottomLeft)):
#             bottom1,top1 = bottomLeft[i],topRight[i]
#             for j in range(i+1,len(topRight)):
#                 bottom2,top2 = bottomLeft[j],topRight[j]
#                 print(bottom1,top1,bottom2,top2)
#                 # find their difference
#                 if bottom1!=bottom2 and bottom1[0]<=bottom2[0]<=top1[0] and bottom1[1]<=bottom2[1]<=top1[1]:
#                     area = (top1[0]-bottom2[0])*(top1[1]-bottom2[1])
#                     print("a")
#                     print(top1,bottom2)
#                     maxarea = max(maxarea,area)
#                     print(area)
#                 if bottom1!= bottom2 and bottom2[0]<=bottom1[0]<=top2[0] and bottom2[1]<=bottom1[1]<=top2[1]:
#                     print("b")
#                     area = (top2[0]-bottom1[0])*(top2[1]-bottom1[1])
#                     area = abs(area)
#                     print(top1,bottom2)
#                     maxarea = max(maxarea,area)
#                     print(area)
#                 if  bottom2[0]<=bottom1[0]<=top2[0] and bottom2[1]<=bottom1[1]<=top2[1]:
#                     print(bottom1,bottom2)
#                     print(bottom2[0],bottom1[0],bottom2[1],bottom1[1])
#                     print("c")
#                     area = (top2[0]-bottom1[0])*(top2[1]-bottom1[1])
#                     print(top1[0],bottom2[0],top1[1],bottom2[1])
#                     area = abs(area)
#                     print(top1,bottom2)
#                     maxarea = max(maxarea,area)
#                     print(area)
#                 if bottom2[0]<=top1[0]<=top2[0] and bottom2[1]<=top1[1]<=top2[1]:
#                     print("d")
#                     area = (top1[0]-bottom2[0])*(top1[1]-bottom2[1])
#                     area = abs(area)
#                     print(top1,bottom2)
#                     maxarea = max(maxarea,area)
#                     print(area)
#         a1 = abs(top1[0]-bottom1[0])*abs(top1[1]-bottom1[1])
#         a2 = abs(top2[0]-bottom2[0])*abs(top2[1]-bottom2[1])
#         ans = min(a1,a2)
#         print(a1,a2,ans)
#         if maxarea>ans:
#             maxarea = ans

#         # find a square number less than maxarea
#         for i in range(maxarea,-1,-1):
#             print(i,math.sqrt(i))
#             if math.sqrt(i) == int(math.sqrt(i)):
#                 return i
#         return 0




        