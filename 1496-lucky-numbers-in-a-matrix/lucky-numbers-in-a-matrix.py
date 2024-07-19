class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        answer= []
        rows = []
        columns = []
        for i in range(len(matrix)):
            minm = float(inf)
            for j in range(len(matrix[0])):
                minm = min(minm,matrix[i][j])
            rows.append(minm)
        for j in range(len(matrix[0])):
            maxm = float(-inf)
            for i in range(len(matrix)):
                maxm = max(maxm,matrix[i][j])
            columns.append(maxm)
        minm_grid = [[0 for i in range(len(matrix[0]))]for j in range(len(matrix))]
        max_grid =  [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
       
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                minm_grid[i][j] = rows[i]
                max_grid[i][j] = columns[j]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if minm_grid[i][j]==max_grid[i][j] == matrix[i][j]:
                    answer.append(matrix[i][j])
        return answer

