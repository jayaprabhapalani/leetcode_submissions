"""
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first get the valid to search
        #so we will perform the valid logic on row lvl

        # 3 scenarios - one for valid case , then if less than target and greater than target

        l=0
        r=len(matrix)-1
        valid_row=0
        while l<=r:
            m=l+(r-l)//2

            #valid row condt
            if matrix[m][0]<= target<=matrix[m][-1]:
                valid_row=m
                break
            elif matrix[m][0]>target:
                r=m-1
            else:
                l=m+1
        
        return self.binary_search_mat(matrix,target,0,len(matrix[0])-1,valid_row)
        
        #binary search on valid index
    def binary_search_mat(self,matrix,target,l,r,valid_row):
        while l<=r:
            mid=l+(r-l)//2
            if matrix[valid_row][mid]==target:
                return True
            elif matrix[valid_row][mid]<target:
                l=mid+1
            else:
                r=mid-1
        return False





        
        
