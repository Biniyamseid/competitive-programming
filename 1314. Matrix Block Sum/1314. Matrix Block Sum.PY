class Solution:
    def matrixBlockSum(self, mat: list[list[int]], K: int) -> list[list[int]]:
        """this is the first day of squid game"""
        """it seems way of survival and many peoples are thinking like that but for me this is the way of the throne. yeah I'm going to my destiny,winning \U0001f496\U0001f496\U0001f496\U0001f496\U0001f496\U0001f496\U0001f496, this is message from Bini,Gennady korotkevich\U0001f60e"""
        m = [[0]*(len(mat[0]) + 1)] + [[0] + row[:] for row in mat]
        for r in range(1, len(m)):
            for c in range(1, len(m[0])):
                m[r][c] += m[r-1][c] + m[r][c-1] - m[r-1][c-1]

        R, C = len(mat), len(mat[0])
        for i in range(R):
            min_r, max_r = max(0, i - K), min(R, i + K + 1)
            for j in range(C):
                min_c, max_c = max(0, j - K), min(C, j + K + 1)
                mat[i][j] = m[max_r][max_c] - m[min_r][max_c] - \
                    m[max_r][min_c] + m[min_r][min_c]
        return mat
