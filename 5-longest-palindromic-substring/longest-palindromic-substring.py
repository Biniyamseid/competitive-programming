class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxm = 0
        sols = []
        answer = ""
        for i in range(len(s)):
            l = r = i
            # length = 0
            while l>=0 and r<len(s) and s[l]==s[r]:
                # length+=1
                l-=1
                r+=1
            cur_maxm = max(r-l-1,maxm)
            if cur_maxm >maxm:
                answer = s[l+1:r]
                maxm = cur_maxm
            sols.append([s[l:r+1],l,r])
            if i<len(s)-1 and s[i]==s[i+1]:
                l,r = i,i+1
                while l>=0 and r<len(s) and s[l]==s[r]:
                    l -=1
                    r +=1
            cur_maxm = max(r-l-1,maxm)
            if cur_maxm >maxm:
                answer = s[l+1:r]
                maxm = cur_maxm
            sols.append(answer)
        print(sols)
        return answer
            


        