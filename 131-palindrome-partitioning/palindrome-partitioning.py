class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """   """
        already = []
        def ispalindrome(string):
            return string == string[::-1]
        def dfs(str,i,visited):
            print(str,i,visited)
            if i == len(s):
                print(visited)
                already.append(visited)
                ans.append(visited[:])
                return
            for j in range(i,len(s)+1):
                print(str[i:j+1],"second loop")
                if ispalindrome(str[i:j+1]):
                    print(str[i:j])
                    dfs(str,j+1,visited+[str[i:j+1]])
        ans = []
        dfs(s,0,[])
        
        return ans
        