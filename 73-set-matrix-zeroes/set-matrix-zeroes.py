class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        #remember if first row/col originally has 0
        first_zero_row=any(matrix[0][j]==0 for j in range(n))
        first_zero_col=any(matrix[i][0]==0 for i in range(m))

        # use first row and col as marker
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        # zero inner cells based on markers
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0

        # handle first row/col last
        if first_zero_row:
            for j in range(n):
                matrix[0][j]=0
        if first_zero_col:
            for i in range(m):
                matrix[i][0]=0