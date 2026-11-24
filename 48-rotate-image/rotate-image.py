class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n=len(matrix)
        matrix2=[row[:] for row in matrix]
        top,bottom=0,len(matrix)-1
        left,right=0,len(matrix[0])-1
        for i in range(len(matrix2[0])):
            res=[]
            for j in range(len(matrix2)-1,-1,-1):
                res.append(matrix2[j][i])
            matrix[i]=res
        
        