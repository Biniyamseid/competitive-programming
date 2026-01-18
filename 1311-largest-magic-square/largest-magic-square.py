class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # prefix sum of each row
        rowsum = [[0] * n for _ in range(m)]
        for i in range(m):
            rowsum[i][0] = grid[i][0]
            for j in range(1, n):
                rowsum[i][j] = rowsum[i][j - 1] + grid[i][j]

        # prefix sum of each column
        colsum = [[0] * n for _ in range(m)]
        for j in range(n):
            colsum[0][j] = grid[0][j]
            for i in range(1, m):
                colsum[i][j] = colsum[i - 1][j] + grid[i][j]

        # enumerate edge lengths from largest to smallest
        for edge in range(min(m, n), 1, -1):
            # enumerate the top-left corner position (i,j) of the square
            for i in range(m - edge + 1):
                for j in range(n - edge + 1):
                    # the value for each row, column, and diagonal should be calculated (using the first row as a sample)
                    stdsum = rowsum[i][j + edge - 1] - (
                        0 if j == 0 else rowsum[i][j - 1]
                    )
                    check = True
                    # enumerate each row and directly compute the sum using prefix sums
                    # since we have already used the first line as a sample, we can skip the first line here.
                    for ii in range(i + 1, i + edge):
                        if (
                            rowsum[ii][j + edge - 1]
                            - (0 if j == 0 else rowsum[ii][j - 1])
                            != stdsum
                        ):
                            check = False
                            break
                    if not check:
                        continue

                    # enumerate each column and directly calculate the sum using prefix sums
                    for jj in range(j, j + edge):
                        if (
                            colsum[i + edge - 1][jj]
                            - (0 if i == 0 else colsum[i - 1][jj])
                            != stdsum
                        ):
                            check = False
                            break
                    if not check:
                        continue

                    # d1 and d2 represent the sums of the two diagonals respectively.
                    # here d denotes diagonal
                    d1 = d2 = 0
                    # sum directly by traversing without using the prefix sum.
                    for k in range(edge):
                        d1 += grid[i + k][j + k]
                        d2 += grid[i + k][j + edge - 1 - k]
                    if d1 == stdsum and d2 == stdsum:
                        return edge

        return 1