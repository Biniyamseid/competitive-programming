class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        canbelast = False
        i =0
        while i<len(bits):
            curr = bits[i]
            if bits[i]==1 and i==len(bits)-1:
                return False
            if bits[i]==1:
                i+=1
                canbelast = False
            elif bits[i]==0:
                # print("hello",i)
                canbelast=True
            i+=1
            # print(i,canbelast,curr)
        return canbelast
    
        