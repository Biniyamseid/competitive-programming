class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        def dfs(i,word,curlist):
            print(i,word,curlist)

            if i == len(s):
                ans.append(curlist)
                return 
            for j in range(i,len(s)+1):
                
                if s[i:j+1] in wordDict:
                    if curlist:
                        dfs(j+1,s[i:j+1],curlist+" " +s[i:j+1])
                    else:
                        dfs(j+1,s[i:j+1],curlist+s[i:j+1])
        dfs(0,s,"")
        return ans

        