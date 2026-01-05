class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        alllist = []
        total = 0
        negatives = []
        count = 0
        for i in  range(len(matrix)):
         for j in range(len(matrix[0])):
            alllist.append(abs(matrix[i][j]))
            if matrix[i][j]<=0:
                negatives.append(matrix[i][j])
            else:
                total+=matrix[i][j]
        if len(negatives)%2==0:
            if negatives:
             total += abs(sum(negatives))
        else:
            if negatives:
                negatives = sorted(negatives,reverse = True)
                total += abs(sum(negatives[1:]))+abs(negatives[0])
                total-= 2*min(alllist)
        return total
            

        