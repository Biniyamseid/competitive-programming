class Solution(object):
    def minDeletionSize(self, A):
        W = len(A[0])
        dp = [1] * W
        for i in range(W-2, -1, -1):
            for j in range(i+1, W):
                if all(row[i] <= row[j] for row in A):
                    dp[i] = max(dp[i], 1 + dp[j])

        return W - max(dp)