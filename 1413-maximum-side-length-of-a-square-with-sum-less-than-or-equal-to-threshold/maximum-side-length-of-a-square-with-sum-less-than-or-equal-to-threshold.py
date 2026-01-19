class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])

        # 1. Build prefix sum matrix
        P = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (
                    mat[i - 1][j - 1]
                    + P[i - 1][j]
                    + P[i][j - 1]
                    - P[i - 1][j - 1]
                )

        # 2. Try square sizes
        def square_exists(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    square_sum = (
                        P[i + k][j + k]
                        - P[i][j + k]
                        - P[i + k][j]
                        + P[i][j]
                    )
                    if square_sum <= threshold:
                        return True
            return False

        # 3. Binary search on side length
        left, right = 0, min(m, n)

        while left < right:
            mid = (left + right + 1) // 2
            if square_exists(mid):
                left = mid
            else:
                right = mid - 1

        return left
