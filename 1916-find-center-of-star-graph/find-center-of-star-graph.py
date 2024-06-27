class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        gra = defaultdict(list)
        for i,j in edges:
            gra[i].append(j)
            gra[j].append(i)
        print(gra)
        for i in gra:
            flag = True
            for j in gra:
                if not i  in gra[j] and j!=i:
                    flag = False
            if flag:
                return i
       
        