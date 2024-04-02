class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ins = set()
        out = set()
        for a,b in zip(s,t):
            ins.add(a)
            out.add(b)
        if len(ins)!= len(out):
            return False
       
        checker = defaultdict(lambda :"0")
        
        notsame = set()
        same = set()

        for a,b in zip(s,t):
            if a in same or b in same:
                if a!=b:
                    return False
            
            if checker[a]!="0":
                if checker[a]==b:
                    pass
                else:
                    print(checker,"first")
                    return False
       

            elif checker[a]=="0":
                checker[a] = b
            
            if a==b:
                same.add(a)
                if a in notsame or b in notsame:
                    return False
                
            else:
                notsame.add(a)
                notsame.add(b)
            

    
        return True
        