
def solution():
    visited = set()
    t = int(input())
    for _ in range(t):
        flag = False
        n,m,sx,sy,d = list(map(int,input().split()))
        res = 0
        n,m,sx,sy= n-1,m-1,sx-1,sy-1
        def dfs(r,c):
            if r<0 or r>n or c<0 or c>m or (r,c) in visited or (abs(r-sx)+abs(c-sy)) <=d: #and distance
                return 0
            visited.add((r,c))
            if (r,c) == (n,m):
                return 1
            neighbours = [(r+1,c),(r,c+1),(r,c-1),(r-1,c)]
            for i,j in neighbours:
                    res =  1+dfs(i,j)
            return res
        print(dfs(0,0))
solution()




        