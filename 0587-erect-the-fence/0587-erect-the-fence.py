class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cmp(p1,p2,p3):
            x1,y1 = p1
            x2,y2 = p2
            x3,y3 = p3
            return ((y3-y2)*(x2-x1))-((y2-y1)*(x3-x2))
        trees.sort()
        upper = []
        lower = []
        for point in trees:
            while len(lower)>1 and cmp(lower[-1],lower[-2],point) >0:
                lower.pop()
            while len(upper)>1 and cmp(upper[-1],upper[-2],point)<0:
                upper.pop()
            upper.append(tuple(point))
            lower.append(tuple(point))
        return list(set(upper+lower))
        
        
                    
    
        