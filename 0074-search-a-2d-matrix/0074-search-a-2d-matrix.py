class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        r = 0
        col = 0
        for i in range(rows):
            l = 0
            r = len(matrix[0])-1
            while l <= r:
                mid = (l+((r-l)//2))
                if matrix[i][mid] > target:
                    r = mid -1
                elif matrix[i][mid]<target:
                    l = mid +1
                else:
                    return True
        return False
        
        
            