class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # traverse from both sides and get the invalid parentheses in set
        omitforward = set()
        stackforward = []
        for i in range(len(s)):

            cur = s[i]
            

            if cur== "(" or cur==")":
                if cur == "(":
                    stackforward.append("(")
                elif not stackforward and cur==")":
                    omitforward.add(i)
                elif stackforward and cur == ")":
                    if stackforward[-1] != "(":
                        omitforward.add(i)
                    elif stackforward[-1] == "(":
                        stackforward.pop()
        omitbackward = set()
        stackbackward = []
        for i in range(len(s)-1,-1,-1):
            cur = s[i]
            if cur == ")" or cur == "(":
                if cur == ")":
                    stackbackward.append(")")
                elif not stackbackward and cur=="(":
                    omitbackward.add(i)
                elif stackbackward and cur == "(":
                    if stackbackward[-1] != ")":
                        omitbackward.add(i)
                    elif stackbackward[-1] == ")":
                        stackbackward.pop()
     
        ans = ""
        for i,letter in enumerate(s):
            if i not in omitforward and i not in omitbackward:
                ans += letter
        

        return ans


        