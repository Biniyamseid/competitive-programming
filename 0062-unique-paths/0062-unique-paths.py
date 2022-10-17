class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for _ in range(n)]for j in range(m)]
        print(matrix)
        lst = [1 for _ in range(n)]
        matrix[m-1] = lst
        print(matrix)
        for h in range(m):
            matrix[h][-1] = 1
        print(matrix)
        for h in range(m-2,-1,-1):
            for k in range(n-2,-1,-1):
                print(h,k)
                matrix[h][k] = matrix[h][k+1]+matrix[h+1][k]
        return matrix[0][0]
    
        
        