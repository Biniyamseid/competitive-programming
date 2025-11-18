class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        canbefirst = False
        i =0
        while i<len(bits):
            curr = bits[i]
            if bits[i]==1 and i==len(bits)-1:
                return False
            if bits[i]==1:
                i+=1
                canbefirst = False
            elif bits[i]==0:
                canbefirst=True
            i+=1
        return canbefirst
    
        