import collections
import math
class DetectSquares:

    def __init__(self):
        self.lst =[]
        

    def add(self, point: list[int]) -> None:
        self.lst.append(point)
        

    def count(self, point: list[int]) -> int:
        self.distance = []
        for i in self.lst:
            distance = int(math.dist(point,i))
            self.distance.append(distance)
       
        res = 0
        count = collections.Counter(self.distance)
        
        for i in count:
            counted = count[i]
           
            if counted>=2 and int(math.sqrt(2)*i) in count and  count[int(math.sqrt(2)*i)]!=0:
                count[i] = 0
                count[int(math.sqrt(2)*i)] -= 1
                
                res += counted-1
        return res



        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)