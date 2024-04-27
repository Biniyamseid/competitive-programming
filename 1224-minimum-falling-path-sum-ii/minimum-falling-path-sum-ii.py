class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        if rows == 1:
            return min(sum(grid,[]))
        @cache
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=columns:
                # print(r,c)
                return 0
                # print(r,c)
                if r >= rows:
                    return 0
                  
                return float("inf")
            a = float("inf")
            for i in range(columns):
                if i!=c:
                    if r<0 or r>=rows or c<0 or c>=columns:
                        if r >=rows:
                            return 0
                        continue
                    a = min(grid[r][c]+dfs(r+1,i),a)
            return a
            # return total
        ans = []

        for i in range(columns):
            ans.append(dfs(0,i))
        # print(ans)
        ans = [i for  i in ans if i and i!= float(inf)]
        return min(ans) if ans else 0

                
        