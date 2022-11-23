class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        R,C=len(grid),len(grid[0])
        vis=set()
        for i in range(R):
            for j in range(C):
                if grid[i][j]!='.':
                    if (grid[i][j]+'found in row'+str(i)) in vis or (grid[i][j]+'found in col'+str(j)) in vis or (grid[i][j]+'found in sub-box'+str(i//3)+"-"+str(j//3)) in vis:return False
                
                    vis.add(grid[i][j]+'found in row'+str(i))
                    vis.add(grid[i][j]+'found in col'+str(j))
                    vis.add(grid[i][j]+'found in sub-box'+ str(i//3)+"-"+ str(j//3))
        return True
                
        