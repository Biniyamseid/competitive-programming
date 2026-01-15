class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        maxvconsec = 0
        maxhconsec = 0
        curr = 0
        conseq = 0
        for i in range(1,len(hBars)):
            if hBars[i]==hBars[i-1]+1:
                if conseq:curr+=1
                else: 
                    curr =2
                    conseq = 1
                maxhconsec= max(maxhconsec,curr)
            else:
                maxhconsec= max(maxhconsec,curr)
                curr=1
                conseq = 0
        curr = 0
        conseq=0
        print(vBars)
        for i in range(1,len(vBars)):
            if vBars[i]==vBars[i-1]+1:
                print("hello")
                if conseq:
                    print("hello1")
                    curr+=1
                else: 
                    curr =2
                    conseq = 1
                maxvconsec= max(maxvconsec,curr)
            else:
                curr=1
                conseq = 0
                maxvconsec= max(maxvconsec,curr)
       
       

        if maxhconsec<1: 
            maxhconsec=1
        if maxvconsec<1: 
            maxvconsec=1
        
        ans = min(maxhconsec,maxvconsec)
        # if len(hBars)==len(vBars):
        #     if ans ==1: return 4
        #     ans-=1
        return (ans+1)*(ans+1)
        

        
        