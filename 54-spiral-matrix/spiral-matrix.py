class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res=[]
        top,bottom=0,len(matrix)-1
        left,right=0,len(matrix[0])-1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1

            for j in range(top,bottom+1):
                res.append(matrix[j][right])
            right-=1

            if top<=bottom:
                for x in range(right,left-1,-1):
                    res.append(matrix[bottom][x])
                bottom-=1
            if left<=right:
                for  w in range(bottom,top-1,-1):
                    res.append(matrix[w][left])
                left+=1
        return res