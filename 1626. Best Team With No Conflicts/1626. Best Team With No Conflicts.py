class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        "dp the timbira"
        scores = zip(scores, ages)
        scores = sorted(scores)
        dp = [scores[i][0] for i in range(len(scores))]
        for i in range(len(scores)):
            for j in range(i):
                if scores[j][1] <= scores[i][1]:
                    dp[i] = max(dp[i], dp[j] + scores[i][0])
        return max(dp)
