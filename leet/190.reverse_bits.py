 def reverseBits(n: int) -> int:
        res = 0
        
        for i in range(32):
            bit = n>>i & 1
            print(n,i,bit)
            res = res | bit << (31 - i)
            print(res)
        return res
#the importance of "|" in res = res | bit << (31 - i)  
#ዪሄ | ለማስቀመጥ አገልግሎት ነው የሚያገለግለው ማለትም ሬዝ ብለን ያስቀመጥነውን ሳንረሳ update lemadreg yemiyageleglen | or bcha new yihe malet 1 kalen be or operator mechem ayitefebnm.




