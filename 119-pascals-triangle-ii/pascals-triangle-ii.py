class Solution:
    hashmap={}
    def helper(self,row,col):
        if row==0 or col==0 or row==col:
            return 1
        key = str(row)+" "+str(col)
        if key in self.hashmap:
            return self.hashmap[key]
        res= self.helper(row-1,col-1) + self.helper(row-1,col)
        self.hashmap[key]=res
        return self.hashmap[key]
    def getRow(self, rowIndex: int) -> list[int]:
        res=[]
        row=rowIndex
        for i in range(rowIndex+1):
            res.append(self.helper(row,i))
        return res