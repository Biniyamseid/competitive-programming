class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        maxvconsec = 1
        maxhconsec = 1
        curr = 1
        for i in range(1,len(hBars)):
            if hBars[i]==hBars[i-1]+1:
                curr+=1
            else:
                curr=1
            maxhconsec= max(maxhconsec,curr)
        curr = 1
        for i in range(1,len(vBars)):
            if vBars[i]==vBars[i-1]+1:
                curr+=1
            else:
                curr=1
            maxvconsec= max(maxvconsec,curr)
       
       

        
        ans = min(maxhconsec,maxvconsec)+1
        return (ans)*(ans)
        

        
        