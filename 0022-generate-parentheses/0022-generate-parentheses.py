class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #ዋናው ሃሳብ n=3 ከ n=2 የሚለየው n =3 ዉስጥ ያሉት ነገሮች በ ተጨማሪ ብራኬት የታሸጉ ናችዉ እና ደግሞ ብራኬቶችን እንደ ቁጥር ማሰብ ነው።
#ብራኬቶችን እንደ ቁጥር ስናስብ ለምሳሌ n = 1 => ["()"] ነው። እና ደግሞ  n=2 =>  ["(())","()()"]
#ስለዚህ 1+2 = 3 => "()"+"(())" = "()(())"
#እና ደግሞ 2 ጃኬት ስትደርብ 3 ትሆናለች። እያንዳንዱ የቁጥር ብራኬት ጃኬት ሲደርብ("በ ብራኬት ሲታቀፍ") በ አንድ ያድጋል። ስለዚህ ማን ምን ትጠብቃለህ ጃኬት እየገዛህ ስጣችዉ እንጂ።
        res = []
        ans = defaultdict(list)
        def bracketadd(word):
            return "("+word+")"
        ans[1].extend(["()"])
        if n<=1:
            return ans[n]
        for i in range(1,n+1):
            mn = 0
            print(ans[i-1],"ans[]")
            for k in ans[i-1]:
                    ans[i].append(bracketadd(k)) 
            for h in range(1,n+1):
                for j in range(1,n+1):
                    if h+j == i:
                        for r1 in ans[h]:
                            for r2 in ans[j]:
                                l = r1+r2
                                ans[i].append(l)
        return list(set(ans[n]))
    
           
        """   res = []
        ans = [[None]]
        def bracketadd(word):
            return "("+word+")"
        ans.append(["()"])
        ans.append(["(())","()()"])
        ans.append(["((()))","(()())","(())()","()(())","()()()"])
        #print(ans[1])
        #print(ans[2])
        print(ans)
        for i in ans[3]:
            res.append(bracketadd(i))
        print(res)
        for i in range(1,4):
            for j in range(1,4):
                if i+j == 4:
                    print(i,j,"this is i,")
                    for r1 in ans[i]:
                        for r2 in ans[j]:
                            res.append(r1+r2)
        print(list(set(res)), "res")
        return list(set(res))
        
        for i in range(1,2):
            print(i)
            print(ans[i])
            for par in ans[i]:
                val = par.split("()")
                print(val)
            print("   ")
            """
        