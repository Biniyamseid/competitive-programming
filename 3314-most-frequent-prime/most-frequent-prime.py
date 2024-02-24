class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            elif n <= 3:
                return True
            elif n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

                    
            
            
        
        answer = []
        
        def dfs(a,b,c,d,cur):
            a+=c
            b+=d
            if a<0 or a>=len(mat) or b<0 or b>=len(mat[0]):
                return
            cur = cur+str(mat[a][b])

            if is_prime(int(cur)):
                if int(cur) >10:
                    answer.append(int(cur))
            # a+=c
            # b+=d
            dfs(a,b,c,d,cur)
            
        dirn = [(0,1),(1,0),(1,1),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                curr = (i,j)
                cur = str(mat[i][j])

                if is_prime(int(cur)):
                    if int(cur) >10:
                        answer.append(int(cur))
                for r,c in dirn:
                    dfs(i,j,r,c,cur)
        if not answer:
            return -1
        
        ans = Counter(answer)

        maxm = -1
        print(answer)
        for i in ans:
            if ans[i] >ans[maxm] or (ans[i]==ans[maxm] and i>maxm):
                maxm = i
        return maxm
                    
        
        