class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of cols
        t = m * n # number of columns
        left = 0
        right = t -1
        while left <= right:
            middle = (left + right) // 2
            i = middle // n # row index
            j = middle % n # column index
            mid_num = matrix[i][j]
            if target == mid_num:
                return True
            elif target <  mid_num:
                right = middle - 1 # search to the left side 
            else:
                left = middle + 1 
            
        return False # exit loop if no target is found

            
        