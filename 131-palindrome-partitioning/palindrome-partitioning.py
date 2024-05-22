class Solution:

    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(i,j):
            return s[i:j+1] == s[i:j+1][::-1]
        """   """
        already = []

        def dfs(i,visited):
            if i == len(s):
                
                already.append(visited)
                ans.append(visited[:])
                return
            for j in range(i,len(s)+1):
                
                if ispalindrome(i,j):
                    
                    dfs(j+1,visited+[s[i:j+1]])
        ans = []
        dfs(0,[])
        
        return ans
        