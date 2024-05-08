class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = reversed(sorted(score))
        dictionary = {}
        for i,val in enumerate(temp):
            dictionary[val] = i+1
        for idx,i in enumerate(score):
            if dictionary[i] == 1:
                score[idx] = "Gold Medal"
            elif dictionary[i] == 2:
                score[idx] = "Silver Medal"
            elif dictionary[i] == 3:
                score[idx] = "Bronze Medal"
            else:
                score[idx] = str(dictionary[i])
        return score

        