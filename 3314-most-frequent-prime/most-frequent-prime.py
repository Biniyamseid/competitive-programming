def Compute():
                # a = max(sum(mat,[]))
                # n =10**(max(len(mat[0]),len(mat)))
                n = 1_000_000
                
                isPrime = [True for i in range(n+1)]
                isPrime[0] = isPrime[1] = False
                p = 2
                while p*p<=n:
                        if isPrime[p]:
                            for i in range(p*p,n+1,p):
                                isPrime[i]=False
                        p+=1
        
                return isPrime
isPrime = Compute()
class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:

        
        answer = []
        
        def dfs(a,b,c,d,cur):
            a+=c
            b+=d
            if a<0 or a>=len(mat) or b<0 or b>=len(mat[0]):
                return
            print(a,b,c,d,cur)
            cur = cur*10+mat[a][b]
            print(cur)
            if isPrime[cur]:
                if int(cur) >10:
                    answer.append(int(cur))
            dfs(a,b,c,d,cur)
            
        dirn = [(0,1),(1,0),(1,1),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                curr = (i,j)
                cur = mat[i][j]
                if isPrime[cur]:
                    if int(cur) >10:
                        answer.append(int(cur))
                for r,c in dirn:
                    dfs(i,j,r,c,cur)
        if not answer:
            return -1
        # print(answer)
        ans = Counter(answer)

        maxm = -1
        for i in ans:
            if ans[i] >ans[maxm] or (ans[i]==ans[maxm] and i>maxm):
                maxm = i
        return maxm
                    
        
        
# class Solution:
#     def mostFrequentPrime(self, mat: List[List[int]]) -> int:
#         n = 1000000
#         isPrime = [True for i in range(n+1)]
#         isPrime[0] = isPrime[1] = False
#         p = 2
#         while p*p<=n:
#             if isPrime[p]:
#                 for i in range(p*p,n+1,p):
#                     isPrime[i]=False
#             p+=1

#         def is_prime(n):
#             return isPrime[n]

#         answer = {}
#         dirn = [(0,1),(1,0),(1,1),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)]

#         def dfs(a,b,c,d,cur):
#             a+=c
#             b+=d
#             if a<0 or a>=len(mat) or b<0 or b>=len(mat[0]):
#                 return
#             cur = cur*10 + mat[a][b]
#             if is_prime(cur) and cur > 10:
#                 answer[cur] = answer.get(cur, 0) + 1
#             dfs(a,b,c,d,cur)

#         for i in range(len(mat)):
#             for j in range(len(mat[0])):
#                 cur = mat[i][j]
#                 if is_prime(cur) and cur > 10:
#                     answer[cur] = answer.get(cur, 0) + 1
#                 for r,c in dirn:
#                     dfs(i,j,r,c,cur)

#         if not answer:
#             return -1
#         maxm = max(answer.keys(),key = lambda x:(answer[x],x)
#         # maxm = max(answer.keys(), key=lambda x: (answer[x], x))
#         # maxm = max(answer, key=answer.get,answer.values)
#         return maxm