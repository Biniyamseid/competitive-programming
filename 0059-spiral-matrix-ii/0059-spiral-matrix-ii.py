class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for row in range(n)]
        row,column = 0,0
        d_r,d_c = 0,1
        count = 1
        while count <= n*n:
            matrix[row][column] = count
            count += 1
            if row + d_r < 0 or row + d_r >= n or column + d_c < 0 or column + d_c >= n or matrix[row+d_r][column+d_c]!=0:
                d_r ,d_c  = d_c,-d_r
            row += d_r
            column += d_c
        return matrix
                
                
        
        
        
        
        
        