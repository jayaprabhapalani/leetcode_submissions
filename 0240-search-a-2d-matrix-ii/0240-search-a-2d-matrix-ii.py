class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # start at last col of first of first row
        m=len(matrix)-1
        n=len(matrix[0])-1
        r=0
        c=n
        while (r<=m and c>=0):
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                c-=1
            else:
                r+=1
        return False
        