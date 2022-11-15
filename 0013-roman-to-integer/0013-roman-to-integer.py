class Solution:
    def romanToInt(self, s):   
        singles = {"I":1,"V" :5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        doubles = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        #my approach is first just find if the current string is in double or not if so increase the current index by two else by one.
        #ወገን
        #ዘልጥ የሚባል ነገር አለ።
        #ሶ
        
        idx = 0
        res = 0
        while idx < len(s):
            if idx <len(s)-1:
                if s[idx:idx+2] in doubles:
                    res += doubles[s[idx:idx+2]]
                    idx += 2
                else:
                    res += singles[s[idx:idx+1]]
                    idx +=1
            else:
                res += singles[s[idx:idx+1]]
                idx +=1
        return res
                
            