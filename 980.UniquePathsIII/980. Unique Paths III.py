class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """determine rows and colums"""
        rows = len(grid)
        cols = len(grid[0])
        """find num of zeros"""
        num_of_zeros = sum([row.count(0) for row in grid])
        self.count = 0  # the final result
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start = (i, j, num_of_zeros)
                    break
        """go deep into the solution"""
        def dfs(i, j, num_of_zeros):
            nonlocal rows
            nonlocal cols
            grid[i][j] = 4
            neigh = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in neigh:
                row = i+dr
                col = j+dc
                if row in range(rows) and col in range(cols):
                    if grid[row][col] == 0:
                        dfs(row, col, num_of_zeros-1)
                    if grid[row][col] == 2 and num_of_zeros == 0:
                        self.count += 1
            grid[i][j] = 0
            return
        dfs(*start)
