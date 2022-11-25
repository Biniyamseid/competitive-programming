class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [[]]
        def isPalindrome(i,j,word):
            while i<j:
                if word[i]!= word[j]:
                    return False
                i+=1
                j-=1
            return True
            
            
        def dfs(index,answer):
            if index == len(s):
                res.append(answer.copy())
                return
            for j in range(index,len(s)):
                if isPalindrome(index,j,s):
                    answer.append(s[index:j+1])
                    dfs(j+1,answer)
                    answer.pop()
        dfs(0,[])
        return res[1:]
                
            
                
        