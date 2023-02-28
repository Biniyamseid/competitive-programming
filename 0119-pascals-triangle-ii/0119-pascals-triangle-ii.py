class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            row = [1]
            return row
        currentRow = [1]
        previousRow = self.getRow(rowIndex-1)
        for i in range(1,rowIndex):
            currentRow.append(previousRow[i-1]+previousRow[i])
        currentRow.append(1)
        return currentRow           
            
       
        
        