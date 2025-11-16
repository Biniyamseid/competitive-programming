class Solution:
    def numSub(self, s: str) -> int:
        #  s = "0110111"
        #  get consecutive ones and append n! for answer
        res = 0
        i = 0
        while (i<len(s)):
                if s[i]=="1":
                    temp_count = 0
                    while i<len(s) and s[i] == "1":
                        temp_count +=1
                        i+=1
                    res += ((temp_count) * (temp_count+1))//2
                else:
                    i+=1
        return res%(10**9+7)
            
        